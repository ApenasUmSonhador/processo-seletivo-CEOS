def particiona(l1, l2):
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
    l1.extend(l2)
    l1 = ordena(l1)

    # Divido a lista, ordenada, como se pede
    meio = len(l1)//2
    l1, l2 = l1[:meio], l1[meio:]

    return l1, l2
