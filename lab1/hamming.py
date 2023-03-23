import numpy as np

class Hamming:
    """
    Class for encoding and decoding 
    """
    gen_matrix = np.array(
        [[1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 1, 1]],
        dtype='int8'
    )

    parity_check_matrix = np.array(
            [[1, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1,0, 1, 0],
            [1, 1, 1, 0, 1, 0, 0]],
            dtype='int8'
    )

    min_error_dict = {
        (0, 0, 0): np.array([0, 0, 0, 0, 0, 0, 0], dtype='int8'),
        (1, 1, 1): np.array([1, 0, 0, 0, 0, 0, 0], dtype='int8'),
        (1, 0, 1): np.array([0, 1, 0, 0, 0, 0, 0], dtype='int8'),
        (0, 1, 1): np.array([0, 0, 1, 0, 0, 0, 0], dtype='int8'),
        (1, 1, 0): np.array([0, 0, 0, 1, 0, 0, 0], dtype='int8'),
        (0, 0, 1): np.array([0, 0, 0, 0, 1, 0, 0], dtype='int8'),
        (0, 1, 0): np.array([0, 0, 0, 0, 0, 1, 0], dtype='int8'),
        (1, 0, 0): np.array([0, 0, 0, 0, 0, 0, 1], dtype='int8')
    }

    @classmethod
    def encode(cls, half_byte:np.array):
        return (half_byte@cls.gen_matrix)%2

    @classmethod
    def decode(cls, hamming_code:np.array):
        check = tuple((cls.parity_check_matrix@hamming_code)%2)
        error = cls.min_error_dict[check]
        return (hamming_code^error)[:4]

    @classmethod
    def create_min_error_dict(cls):
        min_error_dict = {}
        code = np.array([0, 0, 0, 0, 0, 0, 0], dtype='int8')
        min_error_dict[(0, 0, 0)] = code.copy()
        for i in range(len(code)):
            code[i] = 1
            check = tuple(cls.parity_check_matrix@code)
            min_error_dict[check] = code.copy()
            code[i] = 0
        return min_error_dict
