from datetime import date

# Fecha de actualizcion
ultima_actualizacion = date.today()

# Tasas de cambio
tasa_bcv_usd = 23.14
tasa_bcv_eur = 24.89
tasa_usdt = 22.98
tasa_bitcoin_usdt = 23017.02


# Producto
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f'Producto: {self._nombre}, precio: {self._precio}'


producto1 = Producto('PC', 300)

solicitud = input('Hacer cambio a BS, EUR, USDT, BITCOIN. \n Escoge una opción: ')

while solicitud != 'BS' and solicitud != 'EUR' and solicitud != 'USDT' and solicitud != 'BITCOIN':
    print('Solicitud incorrecta, porfavor escribe las siglas correctas: ')
    solicitud = input('Hacer cambio a BS, EUR, USDT, BITCOIN. \n Escoge una opción: ')

if solicitud == 'BS':
    print(f'Precio de la {producto1.nombre} en BS: {producto1.precio * tasa_bcv_usd}')
elif solicitud == 'EUR':
    print(f'Precio de la {producto1.nombre} en EUR: {(producto1.precio * tasa_bcv_usd) / tasa_bcv_eur}')
elif solicitud == 'USDT':
    print(f'Precio de la {producto1.nombre} en USDT: {producto1.precio * tasa_usdt}')
elif solicitud == 'BITCOIN':
    print(
        f'Precio de la {producto1.nombre} en BITCOIN: {((producto1.precio * tasa_bcv_usd) / tasa_usdt) / tasa_bitcoin_usdt}')
