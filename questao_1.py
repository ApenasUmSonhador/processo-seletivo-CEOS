def ler_matriz_do_arquivo(txt):
    matriz = []
    try:
        with open(txt, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                elementos = [int(x) for x in linha.strip().split()]
                matriz.append(elementos)
    except FileNotFoundError:
        print(f"O arquivo '{txt}' não foi encontrado.")
        return None
    return matriz


# Para executar de maneira devida, por favor modificar arquivo
ARQUIVO = "<nome-do-arquivo>.txt"
matriz = ler_matriz_do_arquivo(ARQUIVO)
