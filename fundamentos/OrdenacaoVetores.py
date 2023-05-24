# nome = ["S","a","m","u","e","l"]
# tamanho_vetor = len(nome)
# for i in range(tamanho_vetor):
#     ultima_posicao = tamanho_vetor-(1+i)
#     bola_da_vez = nome[i]
#     rede = nome[ultima_posicao]
#     if ultima_posicao == 2:
#         break
#     nome[ultima_posicao] = bola_da_vez
#     nome[i] = rede
#     print(nome)



#ordenar o vetor [9, 1, 7, 3, 5, 2, 10, 4, 6, 8]
numero = [9, 1, 7, 3, 5, 2, 10, 4, 6, 8]


vetor_tamanho = len(numero)
for i in range(vetor_tamanho):
    posicao_dois = vetor_tamanho-(9+i)
    bola_de_futebol = numero[i]
    gol = numero[posicao_dois]
    numero[posicao_dois] = bola_de_futebol
    numero[i] = gol
    print(numero)