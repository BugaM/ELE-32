from abc import ABC
import csv
import random
from functools import reduce

import numpy as np

class AbstractGraph(ABC):
    def __init__(self, dv, dc, N) -> None:
        self.dv = dv
        self.dc = dc
        self.N = N
        assert dv*N% dc == 0, "dc must dived N*dv"
        self.M = dv*N//dc
        self.max_i = N
        self.c_node_connections = None

    def get_parity_check_mtx(self):
        parity_check_mtx = np.zeros((self.M, self.N), dtype=np.uint8)
        for i, connection in enumerate(self.c_node_connections):
            for node in connection:
                  parity_check_mtx[i][node] = 1
        return parity_check_mtx

    def decode(self, code):
        assert len(code) == self.N, f"Message should be of length N = {self.N}."
        for _ in range(self.max_i):
            # Reset iteration state
            has_error = False
            num_failed_checks = self.N*[0]
            # Check connections
            for connection in self.c_node_connections:
                check = reduce(lambda acc, node: acc ^ bool(code[node]), connection, False)
                # Check failed
                if check:
                    has_error = True
                    for node in connection:
                        num_failed_checks[node] += 1
            # Code is fixed
            if not has_error:
                break
            # Sort nodes by most inequalities parity checks
            num_failed_checks_per_node = sorted(
                enumerate(num_failed_checks), key=lambda x: x[1], reverse=True
            )
            # Flip all bits that have the most number of inequalities
            max_ineq = num_failed_checks_per_node[0][1]
            for node, num_ineq in num_failed_checks_per_node:
                if num_ineq < max_ineq:
                    break
                code[node] = int(not code[node])
        return code
    
    def export_graph(self, path):
        v_node_connections = [[] for i in range(self.N)]
        for i in range(len(self.c_node_connections)):
            v_nodes = self.c_node_connections[i]
            for v_n in v_nodes:
                v_node_connections[v_n].append(i + 1)
        np.savetxt(path, 
           v_node_connections,
           delimiter =",", 
           fmt ='%d')


class RandomGraph(AbstractGraph):
    def __init__(self, dv, dc, N) -> None:
        super().__init__(dv, dc, N)
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
