from abc import ABC
import random
class AbstractGraph(ABC):
      def __init__(self, dv, dc, N) -> None:
            self.dv = dv
            self.dc = dc
            self.N = N
            assert dv*N% dc == 0, "dc must dived N*dv"
            self.M = dv*N//dc

class RandomGraph(AbstractGraph):
      def __init__(self, dv, dc, N) -> None:
            super().__init__(dv, dc, N)
      def build_random_graph(self):
            while True:
                  error= False
                  c_node_connections = [[] for i in range(self.M)]
                  v_node_set = {v: self.dv for v in range(self.N)}
                  for i in range(self.M):
                        try:
                              choices = random.sample(list(v_node_set), self.dc)
                              choices.sort()
                              for choice in choices:
                                    c_node_connections[i].append(choice)
                                    v_node_set[choice] -= 1
                                    if v_node_set[choice] == 0:
                                          del v_node_set[choice]
                        except: error = True
                  if error == False:
                        break
            self.c_node_connections = c_node_connections
