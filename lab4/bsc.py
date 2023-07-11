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


def bits2signal(bits):
      return np.fromiter(map(lambda bit: -1 if bit == 1 else 1, bits), dtype=float)


def gauss_channel_signal(signal, n0):
      variance = 0.5*n0
      return signal + np.random.normal(0, sqrt(variance), np.size(signal))


def bits2noisy_signal(bits, n0):
      return gauss_channel_signal(bits2signal(bits), n0)
