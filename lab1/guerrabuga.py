import random
from math import inf

import numpy as np

class FindGenMatrix:
    """
    Finds a suitable generator matrix for the block code.
    """
    # Rate = 13/22 = 1.03 * 4/7
    K = 13 # Number of message bits
    N = K + 9 # Total number of bits

    # This numbers were choosen, because the rate is similar to 4/7 and
    # the number of syndromes (2**(N-K) = 512) is less than
    # the number of 0 errors (1) plus the number of 1 error (N = 22) plus
    # the number of 2 erros (N*(N-1) = 462), totaling 485.

    # We want to find a generator matrix such that
    # each case of 0, 1 or 2 erros gives out a different syndrome.

    @classmethod
    def create_rand_gen_mx_and_par_check_mx(cls):
        """
        @TODO docstrings and comments
        """
        aux_matrix = np.zeros((cls.K, cls.N - cls.K), dtype='int8')
        numbers = random.sample(range(1, 2**(cls.N - cls.K)), cls.K)
        numbers.sort()
        for i, num in enumerate(numbers):
            for j in range(cls.N - cls.K):
                aux_matrix[i][j] = num%2
                num = num//2
        gen_mx = np.concatenate((np.eye(cls.K, dtype='int8'), aux_matrix), axis=1)
        par_check_mx = np.concatenate((-aux_matrix.T, np.eye(cls.N - cls.K, dtype='int8')), axis=1)%2
        return gen_mx, par_check_mx

    @classmethod
    def eval_mxs(cls, par_check_mx):
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
        syndrome = par_check_mx@error
        syndrome_num = syndrome_to_num(syndrome)
        syndrome_dict[syndrome_num] = error
        for i in range(cls.N):
            error[i] = 1
            syndrome = par_check_mx@error
            syndrome_num = syndrome_to_num(syndrome)
            if syndrome_num in syndrome_dict:
                return False
            syndrome_dict[syndrome_num] = error.copy()
            error[i] = 0
        for i in range(1, cls.N):
            error[i] = 1
            for j in range(i):
                error[j] = 1
                syndrome = par_check_mx@error
                syndrome_num = syndrome_to_num(syndrome)
                if syndrome_num in syndrome_dict:
                    return False
                syndrome_dict[syndrome_num] = error.copy()
                error[j] = 0
            error[i] = 0
        return True

    @classmethod
    def find_mxs(cls, max_iter=inf):
        """
        @TODO docstring
        """
        i = 0
        while i < max_iter:
            i += 1
            gen_mx, par_check_mx = cls.create_rand_gen_mx_and_par_check_mx()
            if cls.eval_mxs(par_check_mx):
                print(f"Matrix found on the {i}-th iteration.")
                # Saving the matrixes
                with open('gen_mx.npy', 'wb') as gen_mx_file:
                    np.save(gen_mx_file, gen_mx)
                with open('par_check_mx.npy', 'wb') as par_check_mx_file:
                    np.save(par_check_mx_file, gen_mx)
                return
        print('Matrixes not found :(')
