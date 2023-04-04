import random
from math import inf

import numpy as np

class FindGenMatrix:
    """
    Finds a suitable generator matrix for the block code.
    """
    # Rate = 13/21 = 1.08 * 4/7
    K = 13 # Number of message bits
    N = K + 8 # Total number of bits

    # This numbers were choosen, because the rate is similar to 4/7 and
    # the number of syndromes (2**(N-K) = 256) is less than
    # the number of 0 errors (1) plus the number of 1 error (N = 21) plus
    # the number of 2 erros (N*(N-1)/2 = 210), totaling 232.

    # We want to find a generator matrix such that
    # each case of 0, 1 or 2 erros gives out a different syndrome.

    @classmethod
    def create_rand_gen_mtx_and_par_check_mtx(cls):
        """
        @TODO docstrings and comments
        """
        aux_mtx = np.zeros((cls.K, cls.N - cls.K), dtype='int8')
        numbers = random.sample(range(1, 2**(cls.N - cls.K)), cls.K)
        numbers.sort()
        for i, num in enumerate(numbers):
            for j in range(cls.N - cls.K):
                aux_mtx[i][j] = num%2
                num = num//2
        gen_mtx = np.concatenate((np.eye(cls.K, dtype='int8'), aux_mtx), axis=1)
        par_check_mtx = np.concatenate((-aux_mtx.T, np.eye(cls.N - cls.K, dtype='int8')), axis=1)%2
        return gen_mtx, par_check_mtx

    @classmethod
    def eval_mtxs(cls, par_check_mtx):
        """
        @TODO docstrings and comments
        """
        def syndrome_to_num(syndrome):
            num = 0
            for bit in syndrome:
                num += 2*num + bit
            return num
        syndrome_dict = {}
        error = np.zeros(cls.N, dtype='int8')
        syndrome = par_check_mtx@error
        syndrome_num = syndrome_to_num(syndrome)
        syndrome_dict[syndrome_num] = error
        for i in range(cls.N):
            error[i] = 1
            syndrome = par_check_mtx@error
            syndrome_num = syndrome_to_num(syndrome)
            if syndrome_num in syndrome_dict:
                return False
            syndrome_dict[syndrome_num] = error.copy()
            error[i] = 0
        for i in range(1, cls.N):
            error[i] = 1
            for j in range(i):
                error[j] = 1
                syndrome = par_check_mtx@error
                syndrome_num = syndrome_to_num(syndrome)
                if syndrome_num in syndrome_dict:
                    return False
                syndrome_dict[syndrome_num] = error.copy()
                error[j] = 0
            error[i] = 0
        return True

    @classmethod
    def find_mtxs(cls, max_iter=inf):
        """
        @TODO docstring
        """
        i = 0
        while i < max_iter:
            i += 1
            gen_mtx, par_check_mtx = cls.create_rand_gen_mtx_and_par_check_mtx()
            if cls.eval_mtxs(par_check_mtx):
                print(f'Matrix found on the {i}-th iteration.')
                # Saving the matrixes
                with open('gen_mtx.npy', 'wb') as gen_mtx_file:
                    np.save(gen_mtx_file, gen_mtx)
                with open('par_check_mtx.npy', 'wb') as par_check_mtx_file:
                    np.save(par_check_mtx_file, par_check_mtx)
                return
        print('Matrixes not found :(')
