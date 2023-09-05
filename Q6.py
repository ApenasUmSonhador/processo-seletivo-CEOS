def particiona(L1, L2):
    """
    Adotei o Quick Sort como maneira ideal e não o Merge Sort
    devido leitura recente do livro 'Entendendo Algoritmos'
    de Aditya Y. Bhargava, Cap 4.
    """
    # Ordenação Quick Sort
    def ordena(lista):
        if len(lista) <= 1:
            return lista

        pivo = lista[len(lista) // 2]
        esquerda = [x for x in lista if x < pivo]
        meio = [x for x in lista if x == pivo]
        direita = [x for x in lista if x > pivo]

        return ordena(esquerda) + meio + ordena(direita)

    # Transformo as 2 listas em uma ordenada
    L1.extend(L2)
    L1 = ordena(L1)

    # Divido a lista, ordenada, como se pede
    meio = len(L1)//2
    L1, L2 = L1[:meio], L1[meio:]

    return L1, L2
l1 = [65455,45,465,46,4,654,9498]
l2 = [65,46,48979,74,979,4,9456487]
l1, l2 = particiona(l1,l2)
print(l1, l2)