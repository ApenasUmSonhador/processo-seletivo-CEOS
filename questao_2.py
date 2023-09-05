# Adotando padrão de leitura da direita para a esquerda.
# Questão 1
def ler_matriz_do_arquivo(txt):
    matriz = []
    try:
        with open(txt, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                elementos = [x for x in linha.strip().split()]
                matriz.append(elementos)
    except FileNotFoundError:
        print(f"O arquivo '{txt}' não foi encontrado.")
        return None
    return matriz


def tira_repetidos(matriz):
    # Tratamento de caso de matriz vazia
    if matriz is None or len(matriz) == 0:
        print("Matriz vazia.")
        return None

    else:
        repete = set()
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if matriz[i][j] in repete:
                    matriz[i][j] = 0
                else:
                    repete.add(matriz[i][j])
        return matriz


# Para executar de maneira devida, por favor modificar arquivo
ARQUIVO = "<nome-do-arquivo>.txt"
matriz = ler_matriz_do_arquivo(ARQUIVO)
matriz = tira_repetidos(matriz)
