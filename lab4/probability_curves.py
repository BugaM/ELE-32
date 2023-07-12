from bsc import prob_to_ssr
import numpy as np
import pickle
from math import log10

import matplotlib.pyplot as plt


P = [0.5,0.2,0.1]


def get_probabilities(P):
      p = []
      while P[-1] > 10**-5:
            p += P
            P = [x/10 for x in P]
      return p
P_BF = [0.05,0.02,0.01]


def get_bitflipping_probs(P):
      p = [0.1]
      while P[-1] >= 10**-5:
            p += P
            P = [x/10 for x in P]
      return p
def db(v):
      if (v > 0):
            return 10*log10(v)
      else: 
            return None

probabilities = get_probabilities(P)

ssr_hamming = [db(prob_to_ssr(p, (4/7))) for p in probabilities]
with open("hamming.pkl", "rb") as fp:   #Pickling
      pe_hamming = pickle.load(fp)
ssr_no_encoding = [db(prob_to_ssr(p,1)) for p in probabilities]
with open("no_encoding.pkl", "rb") as fp:   #Pickling
      pe_no_encoding = pickle.load(fp)


# pe_cycling = [0.500749906261717, 0.278515185601800, 0.0912738590767615,
#                0.0197060036749541, 0.00166247921900976, 0.000254999681250398, 
#                2.99999625000469e-05, 4.99999375000781e-06, 6.24999921875010e-07, 
#                1.87499976562503e-07, 0, 0]

# ssr_cycling = [db(prob_to_ssr(p, (9/17))) for p in probabilities]


bf_probabilities = get_bitflipping_probs(P)
pe_bitflipping = [0.49668599834299915,
 0.3808460519212838,
 0.3103062821372681,
 0.3039968204287453,
 0.24331079645575315,
 0.0196264435246716,
 0.0009885399352637565,
 7.99830036117325e-05,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0,
 0.0]

ssr_bf = [db(prob_to_ssr(p, (4/7))) for p in bf_probabilities]


plt.ymax = 0.5
ax = plt.gca()
plt.yscale("log")
# plt.xscale("log")
plt.xlabel("Ei/N0 (db)")
plt.ylabel("Pe")
plt.xticks([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
ax.set_xlim(0,5)

plt.plot(ssr_hamming, pe_hamming[:len(ssr_hamming)], label="Hamming")
plt.plot(ssr_no_encoding, pe_no_encoding[:len(ssr_no_encoding)], label="No encoding")
# plt.plot(ssr_cycling, pe_cycling[:len(ssr_cycling)], label="Cycling")
plt.plot(ssr_bf, pe_bitflipping[:len(ssr_bf)], label="Bit flipping N=994")
plt.legend()
plt.grid()

plt.show()