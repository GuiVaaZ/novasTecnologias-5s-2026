def transpor_matriz(matriz):
    resultado = []

    for i in range(len(matriz[0])):  # percorre colunas
        nova_linha = []
        for j in range(len(matriz)):  # percorre linhas
            nova_linha.append(matriz[j][i])
        resultado.append(nova_linha)

    return resultado


def multiplicar_matriz(matriz_a, matriz_b):
    # verifica se pode multiplicar
    if len(matriz_a[0]) != len(matriz_b):
        print("Não é possível multiplicar as matrizes")
        return None

    resultado = []

    for i in range(len(matriz_a)):
        linha_resultado = []

        for j in range(len(matriz_b[0])):
            soma = 0
            for k in range(len(matriz_b)):
                soma += matriz_a[i][k] * matriz_b[k][j]

            linha_resultado.append(soma)

        resultado.append(linha_resultado)

    return resultado
