import networkx as nx
import pandas as pd
import numpy as np
import math

class Alg():
    
    listaAbierta = []
    listaCerrada = []
    recorrido = []
    
    def __init__(self, G, origen, destino):
        
        self.G = G
        self.origen = origen
        self.destino = destino
        self.estacionActual = origen
        self.distancia = 0
        self.tiempomin = 0
           
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
                if(self.G.nodes[hijo]['G'] > (self.G.nodes[padre]['G'] + self.G.edges[hijo,padre]['DISTANCIA'])):
                   self.G.nodes[hijo]['G'] = self.G.nodes[padre]['G'] + self.G.edges[hijo,padre]['DISTANCIA']
                   self.calF(hijo)
                   self.G.nodes[hijo]['Padre']= padre
            else:
                self.listaAbierta.append(hijo)
                self.G.nodes[hijo]['G'] = self.G.nodes[padre]['G'] + self.G.edges[hijo,padre]['DISTANCIA']
                self.calF(hijo)
                self.G.nodes[hijo]['Padre']= padre


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
        return c*r
    
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
        self.distancia = round(self.G.nodes[estacion]['G'],4)
        while(self.G.nodes[estacion]['Padre'] != None):
            self.recorrido.insert(0,self.G.nodes[estacion]['Padre'])
            estacion = self.G.nodes[estacion]['Padre']
    
    def tiempo(self):
        x=1
        while(x <len(self.recorrido)):
            self.tiempomin += self.G.edges[self.recorrido[x-1],self.recorrido[x]]['TIEMPO'] 
            x += 1

    def main(self):
        pass