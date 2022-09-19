'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

Grafos - Programa com funções básicas para práticas de algoritmos em grafos.
Classe principal - desenvolvido em Python 3.10.6

05/09/2022
===================================================='''

from igraph import *
from Inicializacao import (dataSet as ds, grafo as g, visualizacao as vis)
from Metodos import (caracteristicas as car)

'''Core do programa'''
def main(instancia):
    print('NOME DA INSTÂNCIA:', instancia, '\n')
    matriz = ds.criaMatrizAdjacencias(instancia)
    print('Matriz de adjacências:')
    print(matriz, '\n')

    listaAdj = ds.criaListaAdjacencias(instancia)
    print('Lista de adjacências:')
    print(listaAdj, '\n')

    G = g.criaGrafo(listaAdj)
    print("Grafo: ")
    print(G, '\n')  # Mostra as características do grafo.
    vis.visualizarGrafo(False, G)  # True para visualização do grafo ou False.

    car.verificaAdjacencia(listaAdj, 0, 1)

    tipo = car.tipoGrafo(listaAdj)
    print("Tipo do grafo: %s " %tipo, '\n')

    car.calcDensidade(listaAdj)

    car.insereVertice(listaAdj, 7)
    print("Inserindo vértice 7: ")
    print(listaAdj, '\n')

    car.insereAresta(listaAdj, 0, 7)
    print("Inserindo aresta (0,7): ")
    print(listaAdj, '\n')

    car.removeAresta(listaAdj, 0, 7)
    print("Removendo vértice 7: ")
    print(listaAdj, '\n')

    car.removeVertice(listaAdj, 7)
    print("Removendo aresta (0,7): ")
    print(listaAdj, '\n')

''' resultado = [instancia, funcao1] # Lista de tipo misto com valores dos resultados
    ds.salvaResultado(resultado) # Salva resultado em arquivo'''

'''Chamada a função main()
   Argumento Entrada: [1] dataset'''
if __name__ == '__main__':
    main(str(sys.argv[1]))

