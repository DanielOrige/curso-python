"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis = índices e fatiamento
Méotodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""


# string = 'ABCDE'
# lista = [123, True, 'Daniel Orige', 1.0, []]

# # print(lista, type(lista))
# # print(bool(lista))
# print(lista)
# print(lista[2], type(lista[2]))
# print(lista[2].upper(), type(lista[2]))
# lista[-3] = 'João'
# print(lista[2], type(lista[2]))

# lista = [10, 20, 30, 40]
# numero = lista[2]
# print(lista)
# print(numero)
# print()

# lista[2] = 300
# numero = lista[2]
# print(lista)
# print(numero)
# print()

# del lista[2]
# numero = lista[2]
# print(lista)
# print(numero)
# print()

# print(lista)
# lista.append(50)
# print(lista)
# lista.append(60)
# print(lista)
# lista.append(70)
# print(lista)
# lista.pop()
# print(lista)
# lista.pop()
# print(lista)
# ultimo_valor = lista.pop()
# print(lista, 'removido:', ultimo_valor)
# ultimo_valor = lista.pop(2)
# print(lista, 'removido:', ultimo_valor)

# lista = [10,20,30,40]
# lista.append('Luiz')
# nome = lista.pop()
# lista.append(1233)
# del lista[-1]
# lista.clear()
# lista.insert(100, 5)
# print(lista, nome)
# print(lista[4])

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b
# lista_d = lista_a.extend(lista_b)
lista_a.extend(lista_b)
print(lista_c)
# print(lista_d)
print(lista_a)