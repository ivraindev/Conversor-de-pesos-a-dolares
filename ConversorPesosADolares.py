menu = """
Bienvenido al conversor de monedas

Elige una opción:

1- Peso colombiano

2- Peso argentino

3- Peso Mexicanos
----------------------
"""
opcion = input (menu)

if opcion == "1":
    pesos = input ("escribre aqui la cantidad en pesos Colombianos: ")
    pesos = float (pesos)
    valor_dolar = 3774.33
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str (dolares)
    print ("Tienes $" + dolares + " dolares")
elif opcion == "2":
    pesos = input ("escribre aqui la cantidad en pesos Argentinos: ")
    pesos = float (pesos)
    valor_dolar = 99
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str (dolares)
    print ("Tienes $" + dolares + " dolares")
elif opcion == "3":
    pesos = input ("escribre aqui la cantidad en pesos Méxicanos: ")
    pesos = float (pesos)
    valor_dolar = 20.50
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str (dolares)
    print ("Tienes $" + dolares + " dolares")
else:
    print ("ingresa una opcion correcta")

