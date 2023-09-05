# Big O final de O(n)
def verifica_permutacao(L1, L2):
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
    if len(L1) != len(L2) or L1 == L2:
        return False
    
    """
    O objetivo aqui é guardar uma contagem de elementos nos dicionários.
    Se os dicionários "baterem" é uma permutação.
    """    
    dict_L1, dict_L2 = preenche_dict(L1), preenche_dict(L2)

    # Retorno se "bate" ou não:
    return dict_L1 == dict_L2

import random

# Criando uma lista aleatória de 9 elementos
lista_aleatoria = random.sample(range(1, 100), 9)

# Criando uma permutação da lista aleatória
lista_permutada = random.sample(lista_aleatoria, len(lista_aleatoria))

print(verifica_permutacao(lista_aleatoria, lista_permutada))