import math

# Função para determinar a precedência dos operadores
def prioridade(operador):
    if (operador in ['+', '-']):
        return 1
    if (operador in ['*', '/']):
        return 2
    if (operador == '^'):
        return 3
    return 0

# Função para verificar se o token é um operador
def isOperador(token):
    return token in ['+', '-', '*', '/', '^']

# Função para verificar se o token é uma função matemática
def isFuncao(token):
    return token in ['sen', 'cos', 'tan', 'cossec', 'sec', 'cotg', 'log']

# Função para avaliar uma expressão na forma pós-fixa (RPN)
def calcularString(fila_organizada, valor_de_x):
    valores = []
    for token in fila_organizada:
        if ((token.replace('.', '').isdigit()) or (token[0] == '-' and token[1:].replace('.', '').isdigit())):
            valores.append(float(token))
        elif (token == 'x'):
            valores.append(valor_de_x)
        elif (token == 'e'):
            valores.append(math.e)
        elif (isOperador(token)):
            num2 = valores.pop()
            num1 = valores.pop()
            if (token == '+'):
                valores.append(num1 + num2)
            elif (token == '-'):
                valores.append(num1 - num2)
            elif (token == '*'):
                valores.append(num1 * num2)
            elif (token == '/'):
                valores.append(num1 / num2)
            elif (token == '^'):
                valores.append(math.pow(num1, num2))
        elif (isFuncao(token)):
            num = valores.pop()
            if (token == 'sen'):
                valores.append(math.sin(num))
            elif (token == 'cos'):
                valores.append(math.cos(num))
            elif (token == 'tan'):
                valores.append(math.tan(num))
            elif (token == 'cossec'):
                valores.append(1 / math.sin(num))
            elif (token == 'sec'):
                valores.append(1 / math.cos(num))
            elif (token == 'cotg'):
                valores.append(1 / math.tan(num))
            elif (token == 'log'):
                valores.append(math.log(num))
    return valores.pop()

# Função para converter uma expressão infixa para pós-fixa (RPN)
def processString(exp):
    operadores = []
    saida = []
    num = ""
    funcao = ""

    for i, c in enumerate(exp):
        if ((c.isdigit()) or (c == '.')):
            num += c
        else:
            if (num):
                saida.append(num)
                num = ""
            if ((c == 'x') or (c == 'e')):
                saida.append(c)
            elif (c == '('):
                operadores.append(c)
            elif (c == ')'):
                while (operadores and operadores[-1] != '('):
                    saida.append(operadores.pop())
                operadores.pop()
                if (operadores and isFuncao(operadores[-1])):
                    saida.append(operadores.pop())
            elif (c.isalpha()):
                funcao += c
                while (i + 1 < len(exp) and exp[i + 1].isalpha()):
                    funcao += exp[i + 1]
                    i += 1
                operadores.append(funcao)
                funcao = ""
            else:
                op = c
                while (operadores and prioridade(operadores[-1]) >= prioridade(c)):
                    saida.append(operadores.pop())
                operadores.append(op)
    
    if (num):
        saida.append(num)

    while (operadores):
        saida.append(operadores.pop())

    return saida

# Função de Bissecção
def bisseccao(x0, x1, precisao, iteracao, fila_organizada):
    k = 0
    while abs(x1 - x0) > precisao and k < iteracao:
        div = (x0 + x1) / 2
        f_div = calcularString(fila_organizada, div)

        print(f"Iteração {k}: x0 = {x0}, x1 = {x1}, div = {div}, f(div) = {f_div}")

        if f_div * calcularString(fila_organizada, x0) < 0:
            x1 = div
        else:
            x0 = div
        k += 1

    print(f"Número de iterações necessárias: {k}")
    return div

# Função da Secante
def sec(x0, x1, precisao, iteracao, fila_organizada):
    k = 0
    while k < iteracao and abs(calcularString(fila_organizada, x1)) > precisao:
        novo = x1 - (calcularString(fila_organizada, x1) * (x1 - x0)) / (calcularString(fila_organizada, x1) - calcularString(fila_organizada, x0))
        x0 = x1
        x1 = novo
        print(f"Valor encontrado a cada iteração: {novo:.8f}, f(x) = {calcularString(fila_organizada, novo):.8f}")
        k += 1

    print(f"Número de iterações necessárias: {k}")
    return x1

# Função de Newton
def newton(x0, precisao, iteracao, fila_organizada, expressao_derivada):
    k = 0
    while k < iteracao and abs(calcularString(fila_organizada, x0)) > precisao:
        novo = x0 - calcularString(fila_organizada, x0) / calcularString(expressao_derivada, x0)
        x0 = novo
        print(f"Valor encontrado a cada iteração: {novo:.8f}, f(x) = {calcularString(fila_organizada, novo):.8f}")
        k += 1

    print(f"Número de iterações necessárias: {k}")
    return x0

# Função Regula Falsi
def regulaFalsi(x0, x1, precisao, iteracao, fila_organizada):
    k = 0
    while k < iteracao and abs(calcularString(fila_organizada, x0)) > precisao and abs(calcularString(fila_organizada, x1)) > precisao:
        novo = (x0 * calcularString(fila_organizada, x1) - x1 * calcularString(fila_organizada, x0)) / (calcularString(fila_organizada, x1) - calcularString(fila_organizada, x0))
        if calcularString(fila_organizada, novo) < 0:
            x0 = novo
        else:
            x1 = novo
        k += 1
        print(f"Valor encontrado a cada iteração: {novo:.8f}, f(x) = {calcularString(fila_organizada, novo):.8f}")

    print(f"Número de iterações necessárias: {k}")
    return novo    

# Função principal
def main():
    expressao = input("Digite a expressao matematica: ")
    fila_organizada = processString(expressao)

    metodo = 0
    while (metodo != 7):
        print("Qual metodo deseja escolher?")
        print("1 - Bissecção")
        print("2 - Secante")
        print("3 - Newton")
        print("4 - Regula Falsi")
        print("5 - deseja mudar a expressão?")
        print("6 - só calcula essa bomba aí")
        print("7 - SAIR")
        metodo = int(input())

        match metodo:
            case 1:
                x0 = float(input("Escolha o valor minimo: "))
                x1 = float(input("Escolha o valor maximo: "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                bisseccao(x0, x1, precisao, iteracao, fila_organizada)

            case 2:
                x0 = float(input("Escolha o valor minimo: "))
                x1 = float(input("Escolha o valor maximo: "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                print(sec(x0, x1, precisao, iteracao, fila_organizada))

            case 3:
                derivada = input("Escreva a derivada da função: ")
                x0 = float(input("Escolha o valor de x0: "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                expressao_derivada = processString(derivada)
                newton(x0, precisao, iteracao, fila_organizada, expressao_derivada)

            case 4:
                x0 = float(input("Escolha o valor minimo: "))
                x1 = float(input("Escolha o valor maximo: "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                print(regulaFalsi(x0, x1, precisao, iteracao, fila_organizada))

            case 5:
                expressao = input("Digite a expressao matematica: ")
                fila_organizada = processString(expressao)

            case 6:
                x0 = float(input("escolha o valor de x: "))
                print(calcularString(fila_organizada, x0))


if __name__ == "__main__":
    main()