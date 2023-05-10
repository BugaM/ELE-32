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

    closest_errors = [
        np.array([0, 0, 0, 0, 0, 0, 0], dtype='int8'),
        np.array([0, 0, 0, 0, 0, 0, 1], dtype='int8'),
        np.array([0, 0, 0, 0, 0, 1, 0], dtype='int8'),
        np.array([0, 0, 0, 1, 0, 0, 0], dtype='int8'),
        np.array([0, 0, 0, 0, 1, 0, 0], dtype='int8'),
        np.array([0, 1, 0, 0, 0, 0, 0], dtype='int8'),
        np.array([0, 0, 1, 0, 0, 0, 0], dtype='int8'),
        np.array([1, 0, 0, 0, 0, 0, 0], dtype='int8')
    ]

    @classmethod
    def encode(cls, half_byte:np.array):
        return (half_byte@cls.gen_matrix)%2

    @classmethod
    def decode(cls, hamming_code:np.array):
        check = (cls.parity_check_matrix@hamming_code)%2
        check_id = check[0] + 2*(check[1] + 2*check[2])
        error = cls.closest_errors[check_id]
        return (hamming_code^error)[:4]

    @classmethod
    def create_closest_errors(cls):
        closest_errors = 8*[[]]
        code = np.array([0, 0, 0, 0, 0, 0, 0], dtype='int8')
        closest_errors[0] = code.copy()
        for i in range(len(code)):
            code[i] = 1
            check = cls.parity_check_matrix@code
            check_id = check[0] + 2*(check[1] + 2*check[2])
            closest_errors[check_id] = code.copy()
            code[i] = 0
        return closest_errors
