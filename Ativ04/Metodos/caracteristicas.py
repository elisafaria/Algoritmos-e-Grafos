'''=================================================
UNIVERSIDADE FEDERAL DE ITAJUBÁ
INSTITUTO DE MATEMÁTICA E COMPUTAÇÃO
SIN110 - ALGORITMOS E GRAFOS
Prof. Rafael Frinhani

caracteristicas - Funções para obtenção das características do grafo e operações em uma matriz de adjacências.

05/09/2022
===================================================='''

'''Verifica Adjacência: Função que verifica se os vértices vi e vj são adjacentes.
Entrada: Lista de adjacencia (Dicionario), vi (Integer), vj (Integer)
Saída: 0 (Integer) se vi e vj NÃO são adjacentes; 1 se vi e vj são adjacentes'''
def verificaAdjacencia(listaAdj, vi, vj):

    if vi in listaAdj and vj in listaAdj[vi]: #se o vértice vj estiver associado ao vértice vi na lista, são adjacentes
        verticesAdjacentes = True
    else:
        verticesAdjacentes = False

    print('Vertices', vi, 'e', vj, 'são adjacentes?', verticesAdjacentes, '\n')
    return verticesAdjacentes


'''Função para verificar as propriedades do grano e retornar o tipo do grafo
Entrada: Lista de adjacencias do tipo dicionário
Saída: (Integer) 0 - Simples; 1 - Digrafo; 2 - Multigrafo; 3 - Pseudografo;'''
def tipoGrafo(listaAdj):
    arestaDirigida = False  # Variável que verifica se existe aresta dirigida
    arestaParalela = False  # Variável que verifica se existe aresta paralela
    lacos = False  # Variável que verifica se existe laços

    for i in listaAdj:
        for j in range(len(listaAdj[i])):
            if listaAdj[i][j] in listaAdj[i][j + 1:]:  # Se a célula M[i][j] for igual a alguma célula M[i][j:] existe uma aresta paralela
                arestaParalela = True
            if i not in listaAdj[listaAdj[i][j]]:  # Se a célula M[i][j] não estiver na lista M[M[i][j]] existe uma aresta dirigida
                arestaDirigida = True
            if i in listaAdj[i]:
                lacos = True

    if not arestaDirigida and not arestaParalela and not lacos:  # Se não tiver aresta pararela, aresta dirigida e laços, o grafo é simples
        tipo = 0
    elif arestaDirigida and not arestaParalela and lacos:  # Se tiver aresta dirigida mas não tiver aresta paralela e laços, o grafo é dirigido
        tipo = 1
    elif not arestaDirigida and arestaParalela and not lacos:  # Se não tiver aresta dirigida nem laços, mas tiver aresta paralela, é um multigrafo
        tipo = 2
    elif not arestaDirigida and arestaParalela and lacos:  # Se não tiver aresta dirigida mas tiver aresta múltiplas e laços, é um pseudografo
        tipo = 3

    return tipo

'''Função para calcular a densidade do grafo
Entrada: Lista de adjacencia (Dicionario)
Saída: (Float) Densidade do grafo'''
def calcDensidade(listaAdj):
    tipo = tipoGrafo(listaAdj)  # Verifica o tipo do grafo

    qtdVertices = len(listaAdj)  # Número de vértices do grafo
    qtdArestas = 0
    for i in range(len(listaAdj)):
        qtdArestas += len(listaAdj[i])  # Contabiliza o número de arestas

    if tipo == 1:  # Se o grafo for dirigido, a quantidade de arestas é dividida por 2 na fórmula
        qtdArestas = qtdArestas / 2

    densidade = qtdArestas / (qtdVertices * (qtdVertices - 1)) #fórmula para calcular a densidade
    densidade = float("{:.3f}".format(densidade))  # Arredonda o valor para 3 casas decimais
    print("Densidade do grafo:", densidade, '\n')

    return densidade


'''Funcão para inserir uma aresta no grafo
Entrada: Lista de adjacencia (Dicionario), vértice de origem (Integer), vértice de destino (Integer)
Saída: Lista de adjacencia com aresta inserida'''
def insereAresta(listaAdj, vi, vj):
    tipo = tipoGrafo(listaAdj)  # Verifica o tipo do grafo
    if vi not in listaAdj or vj not in listaAdj:  # Se o vértice de origem ou o vértice de destino não existir
        print("O vértice não existe")

    if tipo == 1:
        listaAdj[vj].append(vi) # Se o grafo for dirigido, adiciona o vértice de destino na lista de adjacências do vértice de origem
    else:
        listaAdj[vi].append(vj)
        listaAdj[vj].append(vi) #se o grafo não for dirigido, a aresta deve ser inserida da lista dos dois vértices

    return listaAdj

'''Função para inserir um vértice no grafo
Entrada: Lista de adjacencia (Dicionario), vértice a ser inserido (Integer)
Saída: Lista de adjacencia com vértice inserido'''
def insereVertice(listaAdj, vi):

    if vi not in listaAdj:
        listaAdj[vi] = []
    else:
        print("O vértice já existe")

    return listaAdj


'''Função para remover uma aresta do grafo
Entrada: Matriz de adjacências  ou lista de adjacencia (Dicionario), vértice de origem (Integer), vértice de destino (Integer)
Saída: Lista de adjacencia com aresta removida'''
def removeAresta(listaAdj, vi, vj):
    tipo = tipoGrafo(listaAdj)  # Verifica o tipo do grafo
    if vi not in listaAdj or vj not in listaAdj:
        print("O vértice não existe")
    if tipo == 1:
        if vj in listaAdj[vi]:
            listaAdj[vi].remove(vj)
    else:
        listaAdj[vi].remove(vj)
        listaAdj[vj].remove(vi)

    return listaAdj


'''Função para remover um vértice do grafo
Entrada: Lista de adjacencia (Dicionario), vértice a ser removido (Integer)
Saída: Lista de adjacencia com vértice removido'''
def removeVertice(listaAdj, v):

    if v not in listaAdj:
        print("O vértice não existe")
    else:
        del listaAdj[v] # remove a lista de adjacência do vértice
        for i in listaAdj:
            if v in listaAdj[i]:
                listaAdj[i].remove(v) #remove o vértice de outras listas

    return listaAdj

