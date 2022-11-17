import networkx as nx
import pandas as pd
import numpy as np

data = pd.read_csv('metro.csv', sep=';', index_col=False, encoding='cp1252')

G = nx.from_pandas_edgelist(data, source='ORIGEN', target='DESTINO', edge_attr=['DISTANCIA', 'TIEMPO'])
