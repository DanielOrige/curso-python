entrada = input('Você quer "entrar" ou "sair" ').lower()

if entrada == 'entrar':
    print('Você entrou no sistema')
    print(123456789)
elif entrada == 'sair':
    print('Você saiu no sistema')
else:
    print('Você não digitou nem entrar e nem sair')
print('\nFora dos blocos')