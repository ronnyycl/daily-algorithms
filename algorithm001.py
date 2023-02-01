"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


respuesta = 'y'
list = []

# Validacion de respuesta correcta
while respuesta == 'y' or respuesta == 'Y':
    valor = int(input("Introduce un valor: "))
    list.append(valor)
    respuesta = str(input("Deseas añadir otro valor?\n (y) Yes; (n) Not: "))
    if respuesta != 'y' and respuesta != 'n':
        while respuesta != 'y' and respuesta != 'n':
            respuesta = str(input('Respuesta invalida, por favor introduce un valor valido: '))

k = 35
i = 0
suma = 0

while i < len(list):
    for element in list:
        suma = list[i] + element
        if suma == k:
            print(f'{True}, {element} + {list[i]} = {k}')
            i = len(list)
            break

    i += 1




