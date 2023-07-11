from math import erfc, sqrt
from scipy.stats import norm
import numpy as np

def bsc(array, p):
      cpy = array.copy()
      for index, i in enumerate(array):
            random = np.random.random()
            if random < p:
                  cpy[index] = i^1
      return cpy


def get_bitflip_prob(info_energy_noise_ratio, rate):
      return 1 - norm.cdf(sqrt(2*info_energy_noise_ratio*rate))


def gauss_channel_signal(signal, n0):
      variance = 0.5*n0
      return signal + np.random.normal(0, sqrt(variance), np.size(signal))

def prob_to_ssr(prob, rate):
      def calculate_inverse_q_function(p):
            return norm.ppf(1 - p)
      inv_q = calculate_inverse_q_function(prob)
      eb_n0 = 0.5* inv_q**(2)
      return eb_n0/rate

