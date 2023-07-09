from abc import ABC
import random
from functools import reduce

import numpy as np

class AbstractGraph(ABC):
    def __init__(self, dv, dc, N, max_i) -> None:
        self.dv = dv
        self.dc = dc
        self.N = N
        assert dv*N% dc == 0, "dc must dived N*dv"
        self.M = dv*N//dc
        self.max_i = max_i
        self.c_node_connections = None
        self.v_node_connections = None

    def get_parity_check_mtx(self):
        parity_check_mtx = np.zeros((self.M, self.N), dtype=np.uint8)
        for i, connection in enumerate(self.c_node_connections):
            for node in connection:
                  parity_check_mtx[i][node] = 1
        return parity_check_mtx

    def decode(self, r_vec):
        def sum_v_node(v_node):
            c_connection = self.v_node_connections[v_node]
            return r_vec[v_node] + sum(
                edge_cert[(v_node, c_node)] for c_node in c_connection
            )

        assert len(r_vec) == self.N, f"Message should be of length N = {self.N}."
        edge_cert = dict() # key: (v_node, c_node)
        for v_node in range(self.N):
            for c_node in self.v_node_connections[v_node]:
                edge_cert[(v_node, c_node)] = r_vec[v_node]
        for _ in range(self.max_i):
            # Reset iteration state
            has_error = False
            # Check C-Nodes
            for c_node, v_connection in enumerate(self.c_node_connections):
                # Find sign of c node
                sign = reduce(
                    lambda val, x: val*np.sign(x),
                    [edge_cert[(v_node, c_node)] for v_node in v_connection],
                    1
                )
                if sign != 1:
                    has_error = True
                # Find minumum absolut LLR of c node
                min_llr = np.inf
                second_min_llr = np.inf
                has_two_min = False
                for v_node in v_connection:
                    edge_llr = abs(edge_cert[(v_node, c_node)])
                    if edge_llr == min_llr:
                        second_min_llr = min_llr
                        has_two_min = True
                    elif edge_llr < min_llr:
                        second_min_llr = min_llr
                        min_llr = edge_llr
                        has_two_min = False
                    elif edge_llr < second_min_llr:
                        second_min_llr = edge_llr
                        has_two_min = False
                # Calculate sign and absolute llr of each edge
                for v_node in v_connection:
                    edge_sign = sign*np.sign(edge_cert[(v_node, c_node)])
                    old_edge_llr = abs(edge_cert[(v_node, c_node)])
                    edge_llr = (
                        min_llr
                        if has_two_min or old_edge_llr != min_llr
                        else second_min_llr
                    )
                    edge_cert[(v_node, c_node)] = edge_sign*edge_llr
            # Code is fixed
            if not has_error:
                break
            # Change message transmitted by V-Nodes
            for v_node, c_connection in enumerate(self.v_node_connections):
                node_sum = sum_v_node(v_node)
                for c_node in c_connection:
                    edge_cert[(v_node, c_node)] = (
                        node_sum - edge_cert[(v_node, c_node)]
                    )
        # Decode message
        msg = np.array(
            [1 if sum_v_node(v_node) > 0 else 0 for v_node in range(self.N)],
            dtype=np.int8
        )
        return msg
    
    def export_graph(self, path):
        v_node_connections = [
            [c + 1 for c in v_node] for v_node in self.v_node_connections
        ]
        np.savetxt(path, 
           v_node_connections,
           delimiter =",", 
           fmt ='%d')


class RandomGraph(AbstractGraph):
    def __init__(self, dv, dc, N, max_i) -> None:
        super().__init__(dv, dc, N, max_i)
        random.seed(10)
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
        self.v_node_connections = [[] for _ in range(self.N)]
        for i in range(len(self.c_node_connections)):
            v_nodes = self.c_node_connections[i]
            for v_n in v_nodes:
                self.v_node_connections[v_n].append(i)

