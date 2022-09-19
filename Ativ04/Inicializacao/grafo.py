'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

grafo - Funções para criação de um objeto grafo da biblioteca iGraph.
Mais informações: https://igraph.org/python/tutorial/latest/tutorial.html

05/09/2022
===================================================='''

import igraph

'''Cria Grafo: Função para criação de um objeto grafo da biblioteca iGraph a partir de uma lista de adjacências
Entrada: Lista de adjacências (Dicionário)
Saída: grafo (tipo iGraph)'''
def criaGrafo(lista):
    qtdVertices = len(lista)
    grafo = igraph.Graph()  # Cria objeto igraph inicialmente vazio
    grafo.add_vertices(qtdVertices)  # Adiciona vértices ao grafo
    grafo.vs["label"] = range(0, grafo.vcount())  # Define o nome de cada nó como um número inteiro

    for i in lista:
        for j in range(len(lista[i])):
            if i < lista[i][j]:
                grafo.add_edge(i, lista[i][j])

    return grafo