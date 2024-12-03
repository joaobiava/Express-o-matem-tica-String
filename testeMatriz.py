def imprimir_matriz(matriz):
    for linha in matriz:
        print("  ".join(f"{valor}" for valor in linha))

def fatoracao_LU(A, b):
    n = len(A)
    # Inicializa L e U
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]

    # Decomposição LU
    for i in range(n):
        # Calcula elementos de U
        for j in range(i, n):
            soma = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - soma

        # Calcula elementos de L
        for j in range(i, n):
            if i == j:
                L[i][i] = 1  # Diagonal principal de L é 1
            else:
                soma = sum(L[j][k] * U[k][i] for k in range(i))
                L[j][i] = (A[j][i] - soma) / U[i][i]

    print("\nMatriz L:")
    imprimir_matriz(L)
    print("\nMatriz U:")
    imprimir_matriz(U)

    # Resolução de Ly = b
    y = [0] * n
    for i in range(n):
        soma = sum(L[i][k] * y[k] for k in range(i))
        y[i] = (b[i] - soma)

    print("\nVetor Y (solução de Ly = b):")
    print([f"{v:.2f}" for v in y])

    # Resolução de Ux = y
    x = [0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(U[i][k] * x[k] for k in range(i + 1, n))
        x[i] = (y[i] - soma) / U[i][i]

    print("\nVetor X (solução final de Ux = y):")
    print([f"{v:.2f}" for v in x])
    return x

def main():
    ordem = int(input("Digite a ordem da matriz (número de linhas/colunas): "))

    # Entrada da matriz A
    print("\nDigite os valores da matriz A:")
    A = []
    for i in range(ordem):
        linha = list(map(float, input(f"Digite os valores da linha {i + 1} separados por espaço: ").split()))
        A.append(linha)

    # Entrada do vetor b
    print("\nDigite os valores do vetor b:")
    b = list(map(float, input("Digite os valores separados por espaço: ").split()))

    print("\nMatriz A:")
    imprimir_matriz(A)
    print("\nVetor b:")
    print(b)

    print("\nIniciando fatoração LU...")
    fatoracao_LU(A, b)

if __name__ == "__main__":
    main()