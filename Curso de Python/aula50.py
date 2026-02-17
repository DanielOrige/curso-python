"""
Exercício
Exiba os índices da lista
"""

# lista = ['Maria', 'Helena', 'Luiz']
# num = 0

# for nome in lista:
#     print(num, nome, type(nome))
#     num += 1

lista = ['Maria', 'Helena', 'Luiz']
lista.append('Joao')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))