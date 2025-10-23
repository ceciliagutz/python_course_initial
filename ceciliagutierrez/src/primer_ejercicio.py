iva = 16 / 100

''' Calcula el precio con Iva de un producto'''

def mostrar_precio(precio : float) -> float:
 return round((precio*iva) + precio, 2)

print("Ingresa el precio del producto: ")
precio : float = float(input())
print(f'Precio sin Iva: ${precio}\nEl precio con Iva del producto es de: ${mostrar_precio(precio)}')