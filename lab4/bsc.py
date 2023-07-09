from math import erfc, sqrt

import numpy as np

def bsc(array, p):
      cpy = array.copy()
      for index, i in enumerate(array):
            random = np.random.random()
            if random < p:
                  cpy[index] = i^1
      return cpy


def get_bitflip_prob(info_energy_noise_ratio, rate):
      return 0.5*erfc(2*sqrt(info_energy_noise_ratio*rate))     


def gauss_channel_signal(signal, n0):
      variance = 0.5*n0
      return signal + np.random.normal(0, sqrt(variance), np.size(signal))
