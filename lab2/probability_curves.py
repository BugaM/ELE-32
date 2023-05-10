from bsc import bsc
from hamming import Hamming
import numpy as np
import pickle

import matplotlib.pyplot as plt
import matplotlib

PE_CYCLING = [0.500749906261717, 0.278515185601800, 0.0912738590767615,
               0.0197060036749541, 0.00166247921900976, 0.000254999681250398, 
               2.99999625000469e-05, 4.99999375000781e-06, 6.24999921875010e-07, 
               1.87499976562503e-07, 0, 0]
HAMMING_K = 4
P = [0.5,0.2,0.1]


def get_probabilities(P):
      p = []
      while P[-1] > 10**-5:
            p += P
            P = [x/10 for x in P]
      return p

probabilities = get_probabilities(P)

with open("hamming.pkl", "rb") as fp:   #Pickling
      pe_hamming = pickle.load(fp)
with open("no_encoding.pkl", "rb") as fp:   #Pickling
      pe_no_encoding = pickle.load(fp)

plt.ymax = 0.5
ax = plt.gca()
plt.yscale("log")
plt.xscale("log")
# plt.xticks(P)
# plt.yticks(P)
ax.set_xlim(0.5, probabilities[-1])
# ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
# ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
plt.xlabel("p")
plt.ylabel("Pe")

plt.plot(probabilities, pe_hamming, label="Hamming")
plt.plot(probabilities, PE_CYCLING, label="Cycling")
plt.plot(probabilities, pe_no_encoding, label="No encoding")
plt.legend()

plt.show()