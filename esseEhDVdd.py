import math

def avaliarExpressao(expressao, valorX):
    expressao = expressao.replace('x', 'valorX')
    expressao = expressao.replace('^', '**')
    expressao = expressao.replace('sqrt', 'math.sqrt')
    expressao = expressao.replace('e', 'math.e')
    expressao = expressao.replace('pi', 'math.pi')
    expressao = expressao.replace('sin', 'math.sin')
    expressao = expressao.replace('cos', 'math.cos')
    expressao = expressao.replace('tan', 'math.tan')
    expressao = expressao.replace('log', 'math.log10')
    expressao = expressao.replace('ln', 'math.log')
    expressao = expressao.replace('cossec', '1/math.sin')
    expressao = expressao.replace('sec', '1/math.cos')
    expressao = expressao.replace('cotg', '1/math.tan')

    
    resultado = eval(expressao)
    return resultado


def bissec(x0, x1, precisao, iteracao, expressao):
    if (avaliarExpressao(expressao, x0) * avaliarExpressao(expressao, x1) >= 0):
        print("A função não muda de sinal no intervalo dado. O método da bissecção não pode ser aplicado.")
        return None

    for k in range(iteracao):
        x = (x0 + x1) / 2
        if (avaliarExpressao(expressao, x) > 0):
            x1 = x
        else:
            x0 = x
        
        print(f"Iteração {k}: x0 = {x0}, x1 = {x1}, div = {x}, x1 - x0 = {x1 - x0}")

        if (abs(x1 - x0) < precisao):
            return x

    print("O método da bissecção não convergiu dentro do número máximo de iterações.")
    return None

def sec(x0, x1, precisao, iteracao, expressao):
    for k in range(iteracao):
        novo = x1 - avaliarExpressao(expressao, x1) * (x1 - x0) / (avaliarExpressao(expressao, x1) - avaliarExpressao(expressao, x0))
        print(f"iteração: {k}; novo valor: {novo}, f(novo) = {avaliarExpressao(expressao, novo)}")
        if abs(avaliarExpressao(expressao, novo)) < precisao:
            return novo
        x0 = x1 
        x1 = novo

    print("O método da secante não convergiu dentro do número máximo de iterações.")
    return None

def newton(x0, precisao, iteracao, expressao, expressaoDerivada):
    k = 0
    while k < iteracao and abs(avaliarExpressao(expressao, x0)) > precisao:
        novo = x0 - avaliarExpressao(expressao, x0) / avaliarExpressao(expressaoDerivada, x0)
        x0 = novo
        print(f"iteração {k}: Valor encontrado a cada iteração: {novo:.8f}, f(x) = {avaliarExpressao(expressao, novo):.8f}")
        k += 1

    print(f"Número de iterações necessárias: {k}")
    return x0

def regulaFalsi(x0, x1, precisao, iteracao, expressao):
    k = 0
    while k < iteracao and abs(avaliarExpressao(expressao, x0)) > precisao and abs(avaliarExpressao(expressao, x1)) > precisao:
        novo = (x0 * avaliarExpressao(expressao, x1) - x1 * avaliarExpressao(expressao, x0)) / (avaliarExpressao(expressao, x1) - avaliarExpressao(expressao, x0))
        if avaliarExpressao(expressao, novo) < 0:
            x0 = novo
        else:
            x1 = novo
        k += 1
        print(f"iteração: {k} novo valor: {novo:.8f}, f(x) = {avaliarExpressao(expressao, novo):.8f}")

    print(f"Número de iterações necessárias: {k}")
    return novo

def mil(x0, precisao, iteracao, expressao):
    if (abs(avaliarExpressao(expressao, x0)) < precisao):
        print(f"Condição inicial atendida, f(x0) = {avaliarExpressao(expressao, x0)}")
        return x0

    for i in range(iteracao):
        novo = avaliarExpressao(expressao, x0)
        print(f"Iteração {i}: x0 = {x0}, x1 = {novo}, |f(x1)| = {abs(avaliarExpressao(expressao, novo))}")

        if (abs(novo - x0) < precisao):
            return novo
        
        x0 = novo
    print("O método não convergiu dentro do número máximo de iterações.")
    return None

def main():
    print("Exemplo de entrada: -sin(x) + x^2 - 5 + log(10)")
    expressao = input("Digite a expressão matemática (com 'x' como variável): ")

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
                bissec(x0, x1, precisao, iteracao, expressao)

            case 2:
                x0 = float(input("Escolha o valor minimo: "))
                x1 = float(input("Escolha o valor maximo: "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                sec(x0, x1, precisao, iteracao, expressao)

            case 3:
                derivada = input("Escreva a derivada da função: ")
                x = float(input("Escolha o valor de x: "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                newton(x, precisao, iteracao, expressao, derivada)

            case 4:
                x0 = float(input("Escolha o valor minimo: "))
                x1 = float(input("Escolha o valor maximo: "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                print(regulaFalsi(x0, x1, precisao, iteracao, expressao))

            case 5:
                x = float(input("Escolha o valor inicial (x): "))
                iteracao = int(input("Qual o numero maximo de iteracoes: "))
                precisao = float(input("Qual a precisao: "))
                mil(x, precisao, iteracao, expressao)

            case 6:
                expressao = input("Digite a expressao matematica: ")

            case 7:
                x = float(input("escolha o valor de x: "))
                print(avaliarExpressao(expressao, x))


if __name__ == "__main__":
    main()