import numpy as np

def bsc(array, p):
      cpy = array.copy()
      for index, i in enumerate(array):
            random = np.random.random()
            if random < p:
                  cpy[index] = i^1
      return cpy

