saida = ''

def adicao(a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if a or b == 0:
        return 'Não foi possível realizar a divisão por 0'
    else:
        return a / b

def calculadora(a,b,operacao):
    if operacao == '+':
        resultado = adicao(a,b)
    elif operacao == '-':
        resultado = subtracao(a,b)
    elif operacao == '*':
        resultado = multiplicacao(a,b)
    elif operacao == '/':
        resultado = divisao(a,b)
    else:
        resultado = 'Operação inválida'

    return resultado

while saida.lower() != 'n':
    a = float(input('Insira o primeiro número: '))
    b = float(input('Insira o segundo número: '))
    operacao = input('Insira o sinal da operação que deseja realizar(Ex: +, -, * ou /): ')
    resultado = calculadora(a,b,operacao)
    print(f'Resultado da operação: {resultado}')
    saida = input('Deseja continuar?(S/N)').strip().lower()
    if saida == 'n':
        print('Encerrando a calculadora!')