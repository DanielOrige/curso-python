# string = 'ABCDE'
# lista = [123, True, 'Daniel Orige', 1.0, []]

# # print(lista, type(lista))
# # print(bool(lista))
# print(lista)
# print(lista[2], type(lista[2]))
# print(lista[2].upper(), type(lista[2]))
# lista[-3] = 'João'
# print(lista[2], type(lista[2]))

lista = [10, 20, 30, 40]
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

print(lista)
lista.append(50)
print(lista)
lista.append(60)
print(lista)
lista.append(70)
print(lista)
lista.pop()
print(lista)
lista.pop()
print(lista)
ultimo_valor = lista.pop()
print(lista, 'removido:', ultimo_valor)
ultimo_valor = lista.pop(2)
print(lista, 'removido:', ultimo_valor)