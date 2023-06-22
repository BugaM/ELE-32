import pickle as pkl
import numpy as np
from math import ceil
from bsc import bsc
from graph import RandomGraph

SIZE = 201782
MAX_SIZE = SIZE * 50
P = [0.05,0.02,0.01]
WORD_SIZES = [98, 203, 497, 994]

def get_probabilities(P):
      p = [0.1]
      while P[-1] >= 10**-5:
            p += P
            P = [x/10 for x in P]
      return p


def bit_error_rate(info_bits, estimated_bits):
      bit_number = len(info_bits)
      xor = info_bits^estimated_bits
      errors = np.count_nonzero(xor)
      return errors/bit_number


probabilities = get_probabilities(P)

pe_list = []

for word_size in WORD_SIZES:
      graph = RandomGraph(3, 7, word_size)
      pe = []
      for p in probabilities:
            chebishev = ceil(8000/p)
            chebishev = chebishev + word_size - chebishev%word_size
            num_bits = min(chebishev, MAX_SIZE)
            infoword = np.zeros(num_bits, dtype="int64")
            blocks = np.split(infoword, num_bits/word_size)
            print(f"{word_size} -- {p} -- {num_bits}")
            decode = []
            for block in blocks:
                  noised_signal = bsc(block, p) 
                  decode.append(graph.decode(noised_signal))
            pe.append(bit_error_rate(infoword, np.concatenate(decode).ravel()))
      pe_list.append(pe)

print(pe_list)

with open("graph.pkl", "wb") as f:
      pkl.dump(pe_list, f)
