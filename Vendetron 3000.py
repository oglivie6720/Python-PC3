print(''' Vendetron 3000
          El mejor programa para los vendedores en Panama!!
          Izzzz Criminal!!!
      ''')
#Listas []
#Duplas ()
#Diccionarios {}

ventas_globales = 0.0
lista_vendedores = []

while True:
    registro = {}
    nombre = input("\nNombre:  ") #Se introduce el nombre del vendedor.
    while True:
        try:
            venta_mensual = float(input("Venta Mensual: ")) #Se va a leer las ventas.
            break
        except:
            print("Tas metiendo demencia vivo!!!")

    if venta_mensual > 100_000.00:
        print("Eres un vendedor estrella!!!")
    elif venta_mensual > 90000.00:
        print("Te falta poco para la meta!!!")
    elif venta_mensual > 50000:
        print("Sobreviviste :)")
    elif venta_mensual > 0.00:
        print("Larga a vender mas sinverguenza")
    else:
        print("Que haces aqui? DESPEDIDO!!!")

    registro["nombre"] = nombre
    registro["venta"] = venta_mensual
    lista_vendedores.append(registro)


    opcion = input("Desea continuar (S/N)")
    if opcion == 'N' or opcion == 'n':
        break

print("Lista de Vendedores: ")
for x in lista_vendedores:
    print(str(x["nombre"]) + ", ")
    ventas_globales += float(x["venta"])
print("Ventas Globales:", str(ventas_globales))
print("Venta Maxima:" + str(max([x['venta'] for x in lista_vendedores])))
