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
    return token in ['sen', 'cos', 'tan', 'cossec', 'sec', 'cotg', 'log', 'ln']

# Função para avaliar uma expressão na forma pós-fixa (RPN)
def calcularString(filaOrganizada, valor_de_x):
    valores = []
    for token in filaOrganizada:
        if ((token.replace('.', '').isdigit()) or (token[0] == '-' and token[1:].replace('.', '').isdigit())):
            valores.append(float(token))
        elif (token == 'x'):
            valores.append(valor_de_x)
        elif (token == 'e'):
            valores.append(math.e)
        elif (isOperador(token)):
            num2 = valores.pop()
            num1 = valores.pop()

            match token:
                case '+':
                    valores.append(num1 + num2)
                case '-':
                    valores.append(num1 - num2)
                case '*':
                    valores.append(num1 * num2)
                case '/':
                    valores.append(num1 / num2)
                case '^':
                    valores.append(math.pow(num1, num2))

        elif (isFuncao(token)):
            num = valores.pop()
            match token:
                case 'sen':
                    valores.append(math.sin(num))
                case 'cos':
                    valores.append(math.cos(num))
                case 'tan':
                    valores.append(math.tan(num))
                case 'cossec':
                    valores.append(1 / math.sin(num))
                case 'sec':
                    valores.append(1 / math.cos(num))
                case 'cotg':
                    valores.append(1 / math.tan(num))
                case 'log':
                    valores.append(math.log(num))
                case 'ln':
                    valores.append(math.log(num))
    return valores.pop()

# Função para converter uma expressão infixa para pós-fixa (RPN)
def processString(exp):
    operadores = []  # Pilha para operadores e funções
    saida = []  # Lista para notação pós-fixa
    num = ""  # Acumular números
    funcao = ""  # Acumular nomes de funções

    i = 0
    while (i < len(exp)):
        c = exp[i]

        if (c.isdigit() or c == '.'):  # Construir número
            num += c

        else:
            if (num):  # Adicionar número acumulado na saída
                saida.append(num)
                num = ""

            if (c == ' '):
                pass

            elif (c in ['x', 'e']):  # Variáveis ou constantes
                saida.append(c)

            elif (c.isalpha()):  # Nome de função como `ln` ou `sen`
                funcao += c

                while ((i + 1 < len(exp)) and (exp[i + 1].isalpha())):
                    i += 1
                    funcao += exp[i]

                operadores.append(funcao)
                funcao = ""

            elif (c == '('):  # Início de subexpressão
                operadores.append(c)

            elif (c == ')'):  # Fim de subexpressão

                while (operadores and operadores[-1] != '('):
                    saida.append(operadores.pop())

                operadores.pop()  # Remover '('

                if (operadores and isFuncao(operadores[-1])):  # Adicionar função
                    saida.append(operadores.pop())

            elif (isOperador(c)):  # Operadores como +, -, *, etc.

                while (operadores and prioridade(operadores[-1]) >= prioridade(c)):
                    saida.append(operadores.pop())

                operadores.append(c)

        i += 1

    if (num):  # Adicionar último número na saída
        saida.append(num)

    while (operadores):  # Adicionar operadores restantes
        saida.append(operadores.pop())

    return saida

def bissec(x0, x1, precisao, iteracao, filaOrganizada):
    if (calcularString(filaOrganizada, x0) * calcularString(filaOrganizada, x1) >= 0):
        print("A função não muda de sinal no intervalo dado. O método da bissecção não pode ser aplicado.")
        return None

    for k in range(iteracao):
        x = (x0 + x1) / 2
        print(f"Iteração {k}: x0 = {x0}, x1 = {x1}, div = {x}, f(div) = {calcularString(filaOrganizada, x)}")
        if (abs(calcularString(filaOrganizada, x)) < precisao):
            return x
        elif (calcularString(filaOrganizada, x0) * calcularString(filaOrganizada, x) < 0):
            x1 = x
        else:
            x0 = x

    print("O método da bissecção não convergiu dentro do número máximo de iterações.")
    return None

# Função da Secante
def sec(x0, x1, precisao, iteracao, filaOrganizada):
    for _ in range(iteracao):
        novo = x1 - calcularString(filaOrganizada, x1) * (x1 - x0) / (calcularString(filaOrganizada, x1) - calcularString(filaOrganizada, x0))
        if abs(novo - x1) < precisao:
            print(f"Valor encontrado a cada iteração: {novo}, f(novo) = {calcularString(filaOrganizada, novo)}")
            return novo
        x0 = x1 
        x1 = novo

    print("O método da secante não convergiu dentro do número máximo de iterações.")
    return None

# Função de Newton
def newton(x0, precisao, iteracao, filaOrganizada, expressao_derivada):
    k = 0
    while k < iteracao and abs(calcularString(filaOrganizada, x0)) > precisao:
        novo = x0 - calcularString(filaOrganizada, x0) / calcularString(expressao_derivada, x0)
        x0 = novo
        print(f"Valor encontrado a cada iteração: {novo:.8f}, f(x) = {calcularString(filaOrganizada, novo):.8f}")
        k += 1

    print(f"Número de iterações necessárias: {k}")
    return x0

# Função Regula Falsi
def regulaFalsi(x0, x1, precisao, iteracao, filaOrganizada):
    k = 0
    while k < iteracao and abs(calcularString(filaOrganizada, x0)) > precisao and abs(calcularString(filaOrganizada, x1)) > precisao:
        novo = (x0 * calcularString(filaOrganizada, x1) - x1 * calcularString(filaOrganizada, x0)) / (calcularString(filaOrganizada, x1) - calcularString(filaOrganizada, x0))
        if calcularString(filaOrganizada, novo) < 0:
            x0 = novo
        else:
            x1 = novo
        k += 1
        print(f"Valor encontrado a cada iteração: {novo:.8f}, f(x) = {calcularString(filaOrganizada, novo):.8f}")

    print(f"Número de iterações necessárias: {k}")
    return novo

def mil(x0, precisao, iteracao, filaOrganizada):
    if (abs(calcularString(filaOrganizada, x0)) < precisao):
        print(f"Condição inicial atendida, f(x0) = {calcularString(filaOrganizada, x0)}")
        return x0

    for i in range(iteracao):
        novo = calcularString(filaOrganizada, x0)
        print(f"Iteração {i}: x0 = {x0}, x1 = {novo}, |f(x1)| = {abs(calcularString(filaOrganizada, novo))}")

        if (abs(novo - x0) < precisao):
            return novo
        
        x0 = novo
    print("O método não convergiu dentro do número máximo de iterações.")
    return None

def main():
    expressao = input("Digite a expressao matematica: ")
    filaOrganizada = processString(expressao)

    metodo = 0
    while (metodo != 8):
        print("Qual metodo deseja escolher?")
        print("1 - Bissecção")
        print("2 - Secante")
        print("3 - Newton")
        print("4 - Regula Falsi")
        print("5 - MIL")
        print("6 - deseja mudar a expressão?")
        print("7 - só calcula essa bomba aí")
        print("8 - SAIR")
        metodo = int(input())

        match metodo:
            case 1:
                x0 = float(input("Escolha o valor minimo: "))
                x1 = float(input("Escolha o valor maximo: "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                bissec(x0, x1, precisao, iteracao, filaOrganizada)

            case 2:
                x0 = float(input("Escolha o valor minimo: "))
                x1 = float(input("Escolha o valor maximo: "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                print(sec(x0, x1, precisao, iteracao, filaOrganizada))

            case 3:
                derivada = input("Escreva a derivada da função: ")
                x0 = float(input("Escolha o valor de x0: "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                expressao_derivada = processString(derivada)
                newton(x0, precisao, iteracao, filaOrganizada, expressao_derivada)

            case 4:
                x0 = float(input("Escolha o valor minimo: "))
                x1 = float(input("Escolha o valor maximo: "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                print(regulaFalsi(x0, x1, precisao, iteracao, filaOrganizada))

            case 5:
                x0 = float(input("Escolha o valor inicial (x0): "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                mil(x0, precisao, iteracao, filaOrganizada)

            case 6:
                expressao = input("Digite a expressao matematica: ")
                filaOrganizada = processString(expressao)

            case 7:
                x0 = float(input("escolha o valor de x: "))
                print(calcularString(filaOrganizada, x0))


if __name__ == "__main__":
    main()