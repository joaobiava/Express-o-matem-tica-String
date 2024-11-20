def lu_decomposition(matriz):
    """
    Realiza a fatoração LU de uma matriz quadrada.
    Retorna as matrizes L (inferior) e U (superior).
    """
    n = len(matriz)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]

    for i in range(n):
        # Calcula os elementos da matriz U
        for j in range(i, n):
            U[i][j] = matriz[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

        # Calcula os elementos da matriz L
        for j in range(i, n):
            if i == j:
                L[i][i] = 1.0  # Diagonal principal de L é 1
            else:
                L[j][i] = (matriz[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U


def forward_substitution(L, b):
    """
    Resolve o sistema L * y = b por substituição progressiva.
    """
    n = len(L)
    y = [0.0] * n
    for i in range(n):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i)))
    return y


def backward_substitution(U, y):
    """
    Resolve o sistema U * x = y por substituição regressiva.
    """
    n = len(U)
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    return x


def solve_lu(matriz, b):
    """
    Resolve o sistema A * x = b usando a decomposição LU.
    """
    L, U = lu_decomposition(matriz)
    print("Matriz L:")
    print_matriz(L)
    print("Matriz U:")
    print_matriz(U)

    # Resolver L * y = b
    y = forward_substitution(L, b)
    print("Vetor y (solução de L * y = b):")
    print(y)

    # Resolver U * x = y
    x = backward_substitution(U, y)
    print("Vetor x (solução de U * x = y):")
    print(x)

    return x


def print_matriz(matriz):
    """Imprime uma matriz de forma formatada."""
    for row in matriz:
        print(" ".join(f"{elem:8.3f}" for elem in row))
    print()


# Exemplo de uso
if __name__ == "__main__":
    A = [[4, 3, 2],
        [2, 1, 1],
        [6, 5, 4]]
        
    b = [9, 4, 15]  # Vetor de termos independentes

    print("Matriz A:")
    print_matriz(A)
    print("Vetor b:")
    print(b)

    x = solve_lu(A, b)
    print("Solução final do sistema A * x = b:")
    print(x)
