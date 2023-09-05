# Big O final de O(n)
def verifica_permutacao(l1, l2):
    # Função que preencherá dicionários com O(n)
    def preenche_dict(lista):
        dicionario = {}
        for elemento in lista:
            if elemento in dicionario:
                dicionario[elemento] += 1
            else:
                dicionario[elemento] = 1
        return dicionario

    # Tratando caso de tamanhos diferentes e L1 = L2
    if len(l1) != len(l2) or l1 == l2:
        return False

    # O objetivo aqui é guardar uma contagem de elementos nos dicionários.
    # Se os dicionários "baterem" é uma permutação.
    dict_l1, dict_l2 = preenche_dict(l1), preenche_dict(l2)

    # Retorno se "bate" ou não:
    return dict_l1 == dict_l2
