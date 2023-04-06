from bsc import bsc
from hamming import Hamming
from guerrabuga import GuerraBuga
import numpy as np

import matplotlib.pyplot as plt
import matplotlib


SIZE = 1000012
HAMMING_K = 4
GUERRA_BUGA_K = 13
P = [0.5,0.2,0.1]


def get_probabilities(P):
      p = []
      while P[-1] > 10**-5:
            p += P
            P = [x/10 for x in P]
      return p


def bit_error_rate(info_bits, estimated_bits):
      bit_number = len(info_bits)
      xor = info_bits^estimated_bits
      errors = np.count_nonzero(xor)
      return errors/bit_number





information_bits = np.random.randint(2, size = SIZE)

hamming_blocks = np.split(information_bits, SIZE/HAMMING_K)
gb_blocks = np.split(information_bits, SIZE/GUERRA_BUGA_K)


probabilities = get_probabilities(P)

pe_hamming = []
pe_gb = []
pe_no_encoding = []
for p in probabilities:
      hamming_decoded = []
      gb_decoded = []
      for block in hamming_blocks:
            encoded = Hamming.encode(block)
            noised_signal = bsc(encoded, p) 
            hamming_decoded.append(Hamming.decode(noised_signal))
      for block in gb_blocks:
            encoded = GuerraBuga.encode(block)
            noised_signal = bsc(encoded, p) 
            gb_decoded.append(GuerraBuga.decode(noised_signal))
      pe_hamming.append(bit_error_rate(information_bits, np.concatenate(hamming_decoded).ravel()))
      pe_gb.append(bit_error_rate(information_bits, np.concatenate(gb_decoded).ravel()))
      noised_no_encoding = bsc(information_bits, p)
      pe_no_encoding.append(bit_error_rate(information_bits, noised_no_encoding))

plt.ymax = 0.5
ax = plt.gca()
plt.yscale("log")
plt.xscale("log")
plt.xticks(P)
plt.yticks(P)
ax.set_xlim(0.5, probabilities[-1])
ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.xlabel("p")
plt.ylabel("Pe")

plt.plot(probabilities, pe_hamming, label="Hamming")
plt.plot(probabilities, pe_gb, label="GB")
plt.plot(probabilities, probabilities, label="No encoding")
plt.legend()

plt.show()