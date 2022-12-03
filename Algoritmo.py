import networkx as nx
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import json
import os
import csv

class Alg():
    def __init__(self, origen, destino, criterio):
        self.criterio= criterio
        self.origen = origen
        self.destino = destino
        self.estacionActual = origen
        self.principal = 0
        self.secundario = 0
        self.listaAbierta = []
        self.listaCerrada = []
        self.recorrido = []
        self.initGraph()
        self.lineas = []
        self.line = []
        
           
    def getRecorrido(self):
        return self.recorrido
    
    def getLineas(self):
        for x in self.recorrido:
            self.lineas.append(self.G.nodes[x]['Linea'])
        return self.lineas
    
    def transbordosAux(self):
        transbordosAux = []
        with open('transbordos.csv', newline='') as File:  
            reader = csv.reader(File,delimiter=';')
            for row in reader :
                transbordosAux.append(row)
        return transbordosAux
    
    def getTransbordos(self):
        transbordos = []
        transbordosAux = self.transbordosAux()
        for x in range (len(self.lineas)):
            if self.lineas[x] == 0:
                if x > 0 and self.lineas[x-1] == 0:
                    for y in transbordosAux:
                        if self.recorrido[x-1] == y[0] and self.recorrido[x] == y[1]:
                            self.line.append((int)(y[2]))
                elif x > 0 and self.lineas[x-1] != 0:
                    self.line.append(self.lineas[x-1])
                        
                else:
                    if self.lineas[x+1] == 0:
                        for y in transbordosAux:
                            if self.recorrido[x+1] == y[0] and self.recorrido[x] == y[1]:
                                self.line.append((int)(y[2]))
                    else:
                        self.line.append(self.lineas[x+1])
            else:
                self.line.append(self.lineas[x])
        for x in range(len(self.line)-1):
                if(self.line[x]!=self.line[x+1]):
                    transbordos.append(self.recorrido[x])         
        return transbordos

    def algoritmo(self):
        sucesores = []
        solucionEncontrada = False
        self.listaAbierta.append(self.estacionActual)
        self.G.nodes[self.estacionActual]['F']=self.fheuristica(self.estacionActual)
        self.G.nodes[self.estacionActual]['G']=0
        self.G.nodes[self.estacionActual]['Padre']=None
        while(solucionEncontrada == False):
            if(len(self.listaAbierta)<0):
                print("Error.")
                return
            self.estacionActual= self.valFMin()
            self.listaCerrada.append(self.estacionActual)

            self.listaAbierta.remove(self.estacionActual)
            if(self.estacionActual == self.destino ):
                solucionEncontrada =  True
            else:
                sucesores = self.hijos(self.estacionActual)
                for n in sucesores:
                    self.tratarHijo(n,self.estacionActual)
                         
        
    def tratarHijo(self, hijo, padre):
        if((hijo in self.listaCerrada)== False):
            if((hijo in self.listaAbierta)== True):
                if(self.G.nodes[hijo]['G'] > (self.G.nodes[padre]['G'] + self.G.edges[hijo,padre][self.criterio])):
                   self.G.nodes[hijo]['G'] = self.G.nodes[padre]['G'] + self.G.edges[hijo,padre][self.criterio]
                   self.calF(hijo)
                   self.G.nodes[hijo]['Padre']= padre
            else:
                self.listaAbierta.append(hijo)
                self.G.nodes[hijo]['G'] = self.G.nodes[padre]['G'] + self.G.edges[hijo,padre][self.criterio]
                self.calF(hijo)
                self.G.nodes[hijo]['Padre']= padre

    def initGraph(self):
        data = pd.read_csv(os.path.abspath("metro.csv"), sep=';', index_col=False, encoding='cp1252')

        self.G = nx.from_pandas_edgelist(data, source='ORIGEN', target='DESTINO', edge_attr=['DISTANCIA', 'TIEMPO'])

        coords = self.leer(os.path.abspath("Coordenadas.json"))
        for x in coords:
            self.G.nodes[x['Station']]['Coordenadas'] = [x['Latitude'], x['Longitude']]
            self.G.nodes[x['Station']]['Linea'] = x['Line']

    def fheuristica(self, estacion) -> int:
        
        lon1 = np.radians(self.G.nodes[estacion]['Coordenadas'][0])
        lat1 = np.radians(self.G.nodes[estacion]['Coordenadas'][1])
        lon2 = np.radians(self.G.nodes[self.destino]['Coordenadas'][0])
        lat2 = np.radians(self.G.nodes[self.destino]['Coordenadas'][1])
        #radio de la tierra
        r = 6371
        difLat = lat2 - lat1
        difLong = lon2 - lon1
        a = np.sin(difLat/2) ** 2 + np.cos(lat2) * np.cos(lat1) * np.sin(difLong/2) ** 2
        c = 2 * np.arctan2(math.sqrt(a), math.sqrt(1-a))
        if(self.criterio == 'DISTANCIA'):
            return c*r
        elif (self.criterio == 'TIEMPO'):
            return (c*r)/1.3 #Velocidad media metro de atenas
    
    def calF(self, estacion):
        self.G.nodes[estacion]['F'] = self.G.nodes[estacion]['G'] + self.fheuristica(estacion)


    def valFMin(self):
        minValor=float("inf")
        estacion=None
        for n in self.listaAbierta:
            if(self.G.nodes[n]['F']<minValor):
                minValor=self.G.nodes[n]['F']
                estacion=n; 
        return estacion


    def hijos(self, padre):
        sucesores=[]
        for n in nx.neighbors(self.G,padre):
            sucesores.append(n)
        return sucesores

    def camino(self):
        aux=self.listaCerrada.index(self.estacionActual)
        estacion = self.listaCerrada[aux]
        self.recorrido.insert(0,estacion)
        self.principal = round(self.G.nodes[estacion]['G'],4)
        while(self.G.nodes[estacion]['Padre'] != None):
            self.recorrido.insert(0,self.G.nodes[estacion]['Padre'])
            estacion = self.G.nodes[estacion]['Padre']
    
    def otrosCriterios(self):
        x=1
        if(self.criterio == 'TIEMPO'):
            while(x <len(self.recorrido)):
                self.secundario += self.G.edges[self.recorrido[x-1],self.recorrido[x]]['DISTANCIA']
                self.secundario = round(self.secundario,4) 
                x += 1
        else:
             while(x <len(self.recorrido)):
                self.secundario += self.G.edges[self.recorrido[x-1],self.recorrido[x]]['TIEMPO'] 
                x += 1
            
    def leer(self, data):
                with open (data, 'r') as f:
                    coords = json.load(f)
                    f.close()
                return coords

    def main(self):

        self.algoritmo()
        self.camino()   
        self.otrosCriterios()