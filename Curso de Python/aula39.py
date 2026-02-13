# Iterando Strings com While

nome = input("Digite seu nome: ")
novo_nome = ''
contador = 0

while contador < len(nome):
    novo_nome += f'-{nome[contador]}-'
    print(novo_nome)
    contador += 1

contador -= 1

while contador >= 0:
    novo_nome = novo_nome[:-3]
    print(novo_nome)
    contador -= 1