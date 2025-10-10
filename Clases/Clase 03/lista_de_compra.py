# Autor: Mario Santander
"""Crea un programa interactivo que registre productos y calcule información de
la compra.
1. Pedir al usuario el nombre y precio de 3 productos.
2. Guardar los datos en una estructura que permita acceder tanto al
nombre como al precio.
3. Calcular el total a pagar y determinar el producto más caro.
4. Mostrar la lista de productos, el total y cuál fue el producto de mayor
costo."""

print ("------------------------------")
print ("Bienvenido al Registro de productos")
print ("Ingrese los datos de sus 3 productos:")
print ("------------------------------")

# Lista vacía donde guardaremos los productos
productos = []

# Producto 1
nombre = input("Ingrese el nombre del producto 1: ")
precio = float(input(f"Ingrese el precio de {nombre}: "))
productos.append({"nombre": nombre, "precio": precio})

#f"texto {variable}" 
#El prefijo f delante de las comillas indica que es un f-string.
#Dentro del string puedes incrustar variables o expresiones usando {}.
#{nombre} Esto inserta el valor de la variable nombre directamente en el texto.

# El diccionario {"nombre": nombre, "precio": precio} crea un diccionario con dos pares clave–valor:
# "nombre": nombre → la clave "nombre" guarda lo que escribió el usuario en la variable nombre.
# "precio": precio → la clave "precio" guarda el número que escribió el usuario en la variable precio.

#El método append se usa para agregar un nuevo elemento al final de una lista.
#En este caso, agrega el diccionario del producto a la lista productos.

# Producto 2
nombre = input("Ingrese el nombre del producto 2: ")
precio = float(input(f"Ingrese el precio de {nombre}: "))
productos.append({"nombre": nombre, "precio": precio})

# Producto 3
nombre = input("Ingrese el nombre del producto 3: ")
precio = float(input(f"Ingrese el precio de {nombre}: "))
productos.append({"nombre": nombre, "precio": precio})

# Calcular total
total = sum(p["precio"] for p in productos)
#En este caso, p es una variable que representa el total del precio de cada producto de la lista.

# Buscar producto más caro
mas_caro = max(productos, key=lambda x: x["precio"])
#La función max encuentra el elemento con el valor máximo en una lista.
#El parámetro key le dice a max cómo comparar los elementos. En este caso, usamos una función lambda para extraer el precio de cada producto.
#Aquí, lambda x: x["precio"] es una función anónima que toma un elemento x (un diccionario de producto) y devuelve su precio.
#Recorre la lista productos. / De cada producto agarra el "precio". / Busca el producto con el precio más alto. / Devuelve el diccionario completo de ese producto.

# Mostramos La lista de productos y sus precios con decimales
print("\n--- Lista de productos ---")
for p in productos:
    print(f"{p['nombre']}: ${p['precio']:.2f}")

#Esto es un f-string con formato:
#p['nombre'] → accede al valor de la clave "nombre" del producto.
#Ejemplo: "Pan"
#p['precio'] → accede al valor de la clave "precio".
#Ejemplo: 120
#:.2f → formatea el número con 2 decimales (típico en precios).
#120 se muestra como 120.00

print(f"\nTotal a pagar: ${total:.2f}")
print(f"Producto más caro: {mas_caro['nombre']} (${mas_caro['precio']:.2f})")
#terminamos mostrando el total y el producto más caro con su precio formateado a 2 decimales.
#El programa termina aquí.