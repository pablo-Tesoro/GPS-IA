import networkx as nx
import pandas as pd
import numpy as np

edges = pd.read_csv('metro.csv', index_col=None, encoding='cp1252')

G = nx.from_pandas_edgelist(edges, edge_attr=['Distancia(Km)', 'Tiempo (min)'])

G.nodes()
G.edges()
G.order()

for x in G.nodes():
    if G.degree(x) > 2:
        print(x)
        
        