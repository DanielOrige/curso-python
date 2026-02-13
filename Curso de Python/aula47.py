# palavra_secreta = 'games'
# tentativa = 0

# for i in palavra_secreta:
#     tentativa += 1
#     letra_testada = input('Digite uma letra: ')
#     for letra_testada in palavra_secreta:

import os

palavra_secreta = 'games'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabéns')
        print('A palavra era', palavra_secreta)
        print('Quantidade de tentativas: ', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0