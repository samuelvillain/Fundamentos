nome = ["S","a","m","u","e","l"]

for i in range(len(nome)):
    tamanho_vetor = len(nome)
    ultima = tamanho_vetor-(1+i)
    auxiliar = nome[i]
    auxiliar2 = nome[ultima]

    nome[ultima] = auxiliar
    nome[i] = auxiliar2
    print(nome)


#ordenar o vetor [9, 1, 7, 3, 5, 2, 10, 4, 6, 8]

