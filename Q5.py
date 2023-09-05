def acha_maior_3(L):
    # Tratando caso base de L não ter um terceiro elemento e formado apenas por duplicatas
    lista = list(set(L))
    if len(lista) < 3:
        return None

    # Inicializo garantindo que qualquer número é maior que eles
    maior_1 = maior_2 = maior_3 = float('-inf')

    for elemento in lista:
        if elemento > maior_1:
            maior_3 = maior_2
            maior_2 = maior_1
            maior_1 = elemento
            
        elif elemento > maior_2 and elemento != maior_1:
        # Considero "diferente" para tratar o caso de ele ser o repetitivo
        
            maior_3 = maior_2
            maior_3 = elemento
        elif elemento > maior_3 and elemento != maior_1 and elemento != maior_2:
            maior_3 = elemento

    if maior_3 == float("-inf"):
        maior_3 = None
    return maior_3

l = [1,2,3,4,2,3,233,6566,57575,57,757]
print(acha_maior_3(l))