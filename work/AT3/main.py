import matrix

# Transposição
A = [[1, 2], [3, 4], [5, 6]]
print("Matriz A:")
print(A)

transposta = matrix.transpor_matriz(A)
print("Transposta de A:")
print(transposta)


# Multiplicação
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("\nMatriz A:")
print(A)
print("Matriz B:")
print(B)

resultado = matrix.multiplicar_matriz(A, B)
print("Resultado da multiplicação:")
print(resultado)
