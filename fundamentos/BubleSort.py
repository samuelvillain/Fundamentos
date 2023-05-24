def bubble_sort(vetor):
    n = len(vetor)

    # Percorre o vetor n-1 vezes
    for i in range(n - 1):

        # A cada iteração, o maior elemento é colocado no final do vetor
        for j in range(0, n - i - 1):

            # Compara elementos adjacentes
            if vetor[j] > vetor[j + 1]:
                # Troca os elementos se estiverem na ordem errada
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]


# Exemplo de uso
vetor = [9, 5, 7, 2, 1, 8]

print("Vetor antes da ordenação:", vetor)

bubble_sort(vetor)

print("Vetor depois da ordenação:", vetor)
