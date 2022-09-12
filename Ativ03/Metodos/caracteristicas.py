'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''

import numpy as np

#Declarando as Exceptions
class GrafoSimples(Exception):
    pass

class Digrafo(Exception):
    pass

class Multigrafo(Exception):
    pass

class Pseudografo(Exception):
    pass

"""Função que retorna a matriz transposta de uma determinada matriz"""
def transposta(matriz):
    qtdVertices = np.shape(matriz)[0] #verifica o número de linhas da matriz
    t = np.empty((qtdVertices, qtdVertices)) #cria uma matriz do tipo Numpy vazia, com a mesma dimensão da outra
    #troca linhas por colunas
    for l in range(qtdVertices):
        for c in range(qtdVertices):
            t[c][l] = matriz[l][c]
    return t


"""Função para verificar se a matriz é simétrica, fazendo a comparação entre a matriz original e sua transposta.
Se as duas matrizes forem iguais a função retorna True (é simetrica)
Se as duas matrizes forem diferentes a função retorna False (não é simetrica)"""
def verificaSimetria(matriz):
    t = transposta(matriz)
    if (matriz == t).all():
        return True
    else:
        return False


'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: matriz de adjacências (numpy.ndarray), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(matriz, vi, vj):
    if matriz[vi][vj] > 0: # Se célula M[vi][vj] for maior que 0 existe uma ou mais arestas
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False
    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes


'''Tipo Grafo: Função que retorna o tipo do grafo representado por uma matriz de adjacências
Entrada: matriz de adjacências (numpy.ndarray)
Saída: Integer (0 - simples; 1 - dígrafo; 2 - multigrafo; 3 - pseudografo'''
def tipoGrafo(matriz):
    simetrica = verificaSimetria(matriz) #verifica se a matriz é simetrica
    diagonal = matriz.diagonal() #diagonal da matriz
    cont = 0 #contador
    try:
        if not simetrica: #se a matriz não for simetrica, o grafo é dirigido
            raise Digrafo()
        else:
            for linha in matriz:
                for elemento in linha:
                    if elemento != 0 and elemento != 1:#se a matriz tiver valores diferentes de 0 e 1, não é um grafo simples
                        cont += 1
                        break
            if cont != 0:
                for valor in diagonal:
                    if valor != 0: # se a diagonal da matriz possuir valores diferentes de 0, o grafo possui laço(pseudografo)
                        raise Pseudografo()
                    else:
                        raise Multigrafo()
            else:
                raise GrafoSimples()
    except GrafoSimples:
        return 0
    except Digrafo:
        return 1
    except Multigrafo:
        return 2
    except Pseudografo:
        return 3


'''Calcula Densidade: Função que retorna a desidade do grafo representado por uma matriz de adjacências
Entrada: matriz de adjacências (numpy.ndarray)
Saída: Float(valor da densidade com precisão de 3 casas decimais'''
def calcDensidade(matriz):
    qtdVertices = np.shape(matriz)[0]
    arestas = 0
    tipo = tipoGrafo(matriz)
    for linha in matriz:
        for valor in linha:
            arestas += valor #contabiliza o número de arestas na matriz
    #se o grafo não for direcionado, o número de arestas será a soma dos valores indicados na matriz divido por 2(desconsiderando a duplicidade
    if tipo != 1:
        qtdArestas = arestas/2
        D = (2 * qtdArestas)/(qtdVertices*(qtdVertices - 1)) #formula para calcular densidade de grafo simples
    else:
        D = (arestas/(qtdVertices * (qtdVertices - 1))) #formula para calcular densidade de grafo direcionado
    return D

"""Função que insere uma aresta no grafo considerando o par de vértices vi e vj
Entrada: matriz de adjacências (numpy.ndarray) e o par de vértices vi e vj
Saída matriz de adjacências (numpy.ndarray) com a aresta inserida"""
def insereAresta(matriz, vi, vj):
    print("Inserindo aresta na posição (%d, %d):"% (vi, vj))
    tipo = tipoGrafo(matriz)
    matriz[vi - 1][vj - 1] += 1
    #se o grafo não for direcionado, a matriz é simétrica: deve ser acrescentado uma aresta na posição simetrica
    if tipo != 1:
        matriz[vj - 1][vi - 1] += 1 #acrescentando aresta na posição simetrica
    print(matriz, '\n')
    return matriz


"""Função que insere um vértice no grafo
Entrada: matriz de adjacências (numpy.ndarray) e o vértice
Saída matriz de adjacências (numpy.ndarray) com o vértice inserido"""
def insereVertice(matriz, vi):
    qtdVertices = np.shape(matriz)[0]
    if vi <= qtdVertices: #verifica se o vértice já existe
        print("O vértice %d já existe. \n" % vi)
    else:
        print("Inserindo o vértice %d:" %vi)
        matriz = np.insert(matriz, qtdVertices, 0, axis=1) #inserindo coluna
        matriz = np.insert(matriz, qtdVertices, 0, axis=0) #inserindo linha
        print(matriz, '\n')
    return matriz


"""Função que remove uma aresta no grafo considerando o par de vértices vi e vj
Entrada: matriz de adjacências (numpy.ndarray) e o par de vértices vi e vj
Saída matriz de adjacências (numpy.ndarray) com a aresta removida"""
def removeAresta(matriz, vi, vj):
    if matriz[vi-1][vj-1] == 0: # verifica se a aresta existe
        print("A aresta (%d, %d) não existe \n" % (vi, vj))
    else:
        print("Removendo a aresta (%d, %d):" % (vi, vj))
        tipo = tipoGrafo(matriz)
        matriz[vi - 1][vj - 1] -= 1
        # se o grafo não for direcionado, a matriz é simétrica: deve ser removida a aresta na posição simetrica
        if tipo != 1:
            matriz[vj - 1][vi - 1] -= 1 #remove aresta da posição simetrica
    print(matriz, '\n')
    return matriz


"""Função que remove um vértice no grafo
Entrada: matriz de adjacências (numpy.ndarray) e o vértice
Saída matriz de adjacências (numpy.ndarray) com o vértice removido"""
def removeVertice(matriz, vi):
    qtdVertices = np.shape(matriz)[0]
    if vi >= qtdVertices: #verifica se o vértice existe
        print("O vértice %d não existe \n." %vi)
    else:
        print("Removendo o vértice %d:" %vi)
        matriz = np.delete(matriz, (vi - 1), axis=0) #deletando a linha
        matriz = np.delete(matriz, (vi - 1), axis=1) #deletando a coluna
        print(matriz, '\n')
    return matriz
