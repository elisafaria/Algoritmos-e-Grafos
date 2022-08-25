import numpy as np
import sys


#função para ler o arquivo do tipo txt e converter a matriz para o tipo numpy
def leituraArquivo(nome):
    caminho = "C:/Users/faria/OneDrive/Área de Trabalho/ProjetosGrafos/Atividade1/SIN110_-_ATV1_-_Datasets_grafos/" + nome + ".txt"
    with open(caminho, 'r') as arquivo:
        matriz = np.loadtxt(arquivo)
    return matriz


#função para salvar o nome e dimensão da matriz em outro, informações que serão passadas como parâmetro
def salvaResultado(result):
    arq = open('C:/Users/faria/OneDrive/Área de Trabalho/ProjetosGrafos/Atividade1/Resultados/resultado.txt', 'a+')
    arq.writelines(result + '\n')
    arq.close()


if __name__ == "__main__":
    arquivo = sys.argv[1]
    matriz = leituraArquivo(arquivo)
    result = arquivo + ' ' + str(matriz.shape)
    salvaResultado(result)
    print(result)
