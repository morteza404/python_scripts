import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('links.csv')
Graphtype = nx.Graph()
G = nx.from_pandas_edgelist(df, edge_attr='weight', create_using=Graphtype)
nx.draw(G)
plt.show()