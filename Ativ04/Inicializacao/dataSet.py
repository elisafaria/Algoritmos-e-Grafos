'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

dataSet - Funções de leitura de um dataset, criação das estruturas de representação de grafos e salvamento de resultados em arquivo.

05/09/2022
===================================================='''

import numpy as np

'''Cria Matriz de Adjacência: Função para leitura de um dataset em forma de matriz de adjacências.
Entrada: instancia (nome do arquivo .txt do dataset em forma de matriz de adjacência
Saída: matriz de adjacência (tipo NumPy.ndarray)'''
def criaMatrizAdjacencias(instancia):
    caminho = 'C:/Users/faria/OneDrive/Documentos/Repositorios/AlgoritmosEGrafos/Ativ04/Instancias/' + instancia + '.txt'
    with open(caminho, 'rb') as f:
        data = np.genfromtxt(f, dtype="int64") #OBS. Lê arquivo .txt de uma Instancia no formato Matriz de Adjacência
    return data

'''Salva Resultado: Função para salvar em arquivo .txt o resultado da execução do programa.
Entrada: resultado (tipo lista)
Saída: arquivo .txt no diretório especificado'''
def salvaResultado(resultado):
    stringRes = ''
    for res in resultado:
        stringRes += str(res) + ' '
    arquivo = open('C:/Users/faria/OneDrive/Documentos/Repositorios/AlgoritmosEGrafos/Ativ04/Resultados/resultado.txt', 'a+')
    arquivo.writelines(stringRes + '\n')
    arquivo.close()

'''Cria Lista de Adjacências: Função para leitura de um dataset em forma de lista de adjacências.
Entrada: instancia (nome do arquivo .txt do dataset em forma de lista de adjacência
Saída: lista de adjacência (tipo Dicionário)'''
def criaListaAdjacencias(instancia):
    matriz = criaMatrizAdjacencias(instancia) #cria a matriz de adjacencias a partir do dataset
    lista = {} #lista do tipo dicionário
    for i in range(len(matriz)):
        lista[i] = [] #cria um vetor para cada linha da matriz
        for j in range(len(matriz)):
            if matriz[i][j] > 0: #verifica se existe aresta
                for k in range(matriz[i][j]):
                    lista[i].append(j)
    return lista