# Questão 1
def ler_matriz_do_arquivo(txt):
    matriz = []
    try:
        with open(txt, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                elementos = [x for x in linha.strip().split()]
                matriz.append(elementos)
    except FileNotFoundError:
        print(f"O arquivo '{txt}' não foi encontrado.")
        return None
    return matriz

def mostra_matriz(matriz):
    # Tratamento de caso de matriz vazia
    if matriz is None or len(matriz) == 0:
        print("Matriz vazia.")
        return
    # Optei por separar os elementos de uma mesma linha por um tab.
    for linha in matriz:
        for elemento in linha:
            print(elemento, end='\t')
        print()

# Para executar de maneira devida, por favor modificar arquivo
ARQUIVO = "<nome-do-arquivo>.txt"
matriz = ler_matriz_do_arquivo(ARQUIVO)
mostra_matriz(matriz)
