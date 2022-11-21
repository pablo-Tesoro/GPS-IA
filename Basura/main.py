import networkx as nx
import pandas as pd
import numpy as np
from Algoritmo import Alg
import matplotlib.pyplot as plt
import json
import os

def leer(data):
        with open (data, 'r') as f:
            coords = json.load(f)
            f.close()
        return coords

data = pd.read_csv("metro.csv", sep=';', index_col=False, encoding='cp1252')

G = nx.from_pandas_edgelist(data, source='ORIGEN', target='DESTINO', edge_attr=['DISTANCIA', 'TIEMPO'])


coords = leer("Coordenadas.json")
for x in coords:
    G.nodes[x['Station']]['Coordenadas'] = [x['Latitude'], x['Longitude']]
    G.nodes[x['Station']]['Linea'] = x['Line']

al = Alg(G, 'Piraeus',  'Aghios Antonios')
al.algoritmo()
print(al.listaCerrada)
al.camino()
print(al.recorrido)
print(al.distancia)
al.tiempo()
print(al.tiempomin)



#for n in nx.neighbors(G, 'Faliro'):
    #print (n)
#print(np.radians(float(G.nodes['Faliro']['Coordenadas'][0])))
#print(G.get_edge_data('Piraeus', 'Faliro'))
