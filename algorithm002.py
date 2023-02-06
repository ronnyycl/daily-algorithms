"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

lista = [3, 2, 1]
i = 0
lista_nueva = []

while i < len(lista):
    numero = lista[i]
    indice = lista.index(numero)
    valor = 1
    for element in lista:
        if lista.index(element) != indice:
            valor *= element
    lista_nueva.append(valor)
    i += 1

print(lista_nueva)

"""
Line - 11. Se inicializa una lista que posee determinados valores.
Line - 12. Se establece una variable i, el cual sera el contador de la veces en que se ejecutara el ciclo
Line - 13. lista_nueva, variable definida como la lista que contendra el resultado de los  valores adquiridos
Line - 15. Ciclo while, este ciclo sera el iterador de todos los valores alojados en la lista (Variable Line 11)
Line - 16. Dentro del ciclo While, se crea una variable llamada numero que aloja el valor de la posición lista[i]
            Ejemplo: numero = lista[i=0]; numero = 3
Line - 17. Variable indice, aloja los indices de cada valor de la variable lista
Line - 18. Variable valor, definida como valor inicial entero 1. Usada para alojar la multiplicación valores
            (permitidos)
Line - 19. Apertura del Ciclo for para iterar cada elemento en la lista y asi ser multiplicado
Line - 20. Condicional, donde se evalua si el indice guardado sera igual al del elemento para evitar que se 
            multiplique a si mismo
Line - 21. Multiplicación de los elementos que son diferentes al indice del numero usado y siendo alojados en valor
Line - 22  Valor hallado, siendo agregado a traves del metodo append hacia una lista nueva
Line - 23   Aumento del valor de  la variable i
Line - 25   Impresión de la nueva lista
         
"""





