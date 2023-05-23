def alterar_diagonal_principal(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
          if  ((i == 0 and j == 0) or
            (i == 1 and j == 1) or
            (i == 2 and j == 2)):
            matriz[i][j] = valor


def diagonal_secundaria(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if ((i == 0 and j == 2) or
                    (i == 2 and j == 0)):
                matriz[i][j] = valor




def imprimir_matriz(matriz):
    for vetor in matriz:
        print(vetor)



def funcao_teste(nome, sobrenome, pqp):
    print("Teste: ", nome, sobrenome, pqp)

if __name__ == "__main__":
    funcao_teste("Villain","Roberto", 21)
    # matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    # alterar_diagonal_principal(matriz, 10)
    # diagonal_secundaria(matriz, 20)
    # imprimir_matriz(matriz)

