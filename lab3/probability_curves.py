from bsc import bsc
import numpy as np
import pickle

import matplotlib.pyplot as plt
import matplotlib

# PE_CYCLING = [0.500749906261717, 0.278515185601800, 0.0912738590767615,
#                0.0197060036749541, 0.00166247921900976, 0.000254999681250398, 
#                2.99999625000469e-05, 4.99999375000781e-06, 6.24999921875010e-07, 
#                1.87499976562503e-07, 0, 0]
HAMMING_K = 4
P = [0.05,0.02,0.01]


def get_probabilities(P):
      p = [0.1]
      while P[-1] >= 10**-5:
            p += P
            P = [x/10 for x in P]
      return p

probabilities = get_probabilities(P)

with open("hamming.pkl", "rb") as fp:   #Pickling
      pe_hamming = pickle.load(fp)
with open("no_encoding.pkl", "rb") as fp:   #Pickling
      pe_no_encoding = pickle.load(fp)
with open("graph.pkl", "rb") as fp:
      pe_graphs = pickle.load(fp)

plt.ymax = 0.5
ax = plt.gca()
plt.yscale("log")
plt.xscale("log")
ax.set_xlim(0.1, probabilities[-1])
plt.xlabel("p")
plt.ylabel("Pe")

plt.plot(probabilities, pe_hamming[2:], label="Hamming")
plt.plot(probabilities, pe_no_encoding[2:], label="No encoding")
plt.plot(probabilities, pe_graphs[0], label="100")
plt.plot(probabilities, pe_graphs[1], label="200")
plt.plot(probabilities, pe_graphs[2], label="500")
plt.plot(probabilities, pe_graphs[3], label="1000")
plt.legend()

plt.show()