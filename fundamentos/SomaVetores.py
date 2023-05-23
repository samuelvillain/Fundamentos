vetor1 = [1, 2, 3, 4]
vetor2 = [5, 6, 7, 8]
vetor3 = [0, 0, 0, 0]

matriz1 = [vetor2, vetor1]

for posicao in range(len(vetor1)):
    vetor3[posicao] = vetor1[posicao] + vetor2[posicao]

print(vetor3)




#for i in range(len(matriz1)):
#    for j in range(len(matriz1[i])):
#       elemento = matriz1[i][j]
#        matriz1[i][j] = elemento * 2

#for elemento in matriz1:
#    print(elemento)
