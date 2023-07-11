import pickle as pkl
import numpy as np
from hamming import Hamming
from bsc import  gauss_channel_signal
from graph import RandomGraph

SIZE = 201782
MAX_SIZE = SIZE

HAMMING_K = 4
EB = 1

EB_NO_DB = np.linspace(0,5,11)


def get_NO(eb, eb_no_db):
      eb_n0 = 10**(eb_no_db/10)
      n0 = eb/eb_n0
      return n0



def bit_error_rate(info_bits, estimated_bits):
      bit_number = len(info_bits)
      xor = info_bits^estimated_bits
      errors = np.count_nonzero(xor)
      return errors/bit_number

pe_list = []

word_size = 98
graph = RandomGraph(3, 7, word_size, 10)
ei_n0 = []

pe_hamming = []
pe = []
for ratio in EB_NO_DB:
      num_bits = (MAX_SIZE)
      n0 = get_NO(EB, ratio)
      Ei = EB/(4/7)
      infoword = np.zeros(num_bits, dtype="int64")

      blocks = np.split(infoword, num_bits/word_size)
      print(f"{word_size} -- {ratio} -- {num_bits}")
      decode = []
      for block in blocks:
            noised_signal = gauss_channel_signal(block, n0) 
            decode.append(graph.decode(noised_signal))
      ei_n0.append(Ei/n0)
      pe.append(bit_error_rate(infoword, np.concatenate(decode).ravel()))
pe_list.append(pe)

print(pe_list)

with open("ldpc_gaussian.pkl", "wb") as f:
      pkl.dump(pe_list, f)
with open("ei_no_gaussian.pkl", "wb") as f:
      pkl.dump(ei_n0, f)