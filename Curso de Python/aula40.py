# Calculadora com While

numero1 = 0
numero2 = 0
operador = ''
continuar = True

while continuar:
    numero1 = int(input('Digite o primeiro número: '))
    numero2 = int(input('Digite o segundo número: '))
    operador = input('Digite o operador (+) (-) (*) (/): ')
    print(' ')

    if operador == '+':
        print('Resultado =', numero1 + numero2)
    elif operador == '-':
        print('Resultado =', numero1 - numero2)
    elif operador == '*':
        print('Resultado =', numero1 * numero2)
    elif operador == '/':
        if numero2 == 0:
            print('Não é possível realizar divisão por zero')
        else:
            print('Resultado =', numero1 / numero2)
    else:
        print('Nenhum operador válido digitado')
    print(' ')

    continuar = input('Deseja continuar ? (s) (n): ')
    if continuar == 'n':
        break
    print('')
