import numpy as np
import networkx as nx

A = np.genfromtxt(
    "res/network.txt", delimiter=",", missing_values="-", filling_values=0
)
G = nx.from_numpy_matrix(A)
mst = nx.minimum_spanning_tree(G)
total_weight = lambda G: sum(nx.get_edge_attributes(G, "weight").values())
print(total_weight(G) - total_weight(mst))
