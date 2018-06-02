print("\t\t\t\t\t\t\t\tPrograma que te permite transformar de decimal a binario y viceversa.")


numeroDecimal=0
numeroBinario=""
res=0

opcion = input("Si desea transformar a binario toque b o B, si desea transformar a decimal toque d o D:   ")
while True:
    while True:
          if opcion == 'B' or opcion == 'b':
            print("Número decimal a binario")
            numeroDecimal=int(input('Introduce número decimal:'))
            print("Número decimal leido: ",numeroDecimal)
            while (numeroDecimal>=2):
                res=numeroDecimal%2
                numeroDecimal=(int)(numeroDecimal/2)
                numeroBinario+=(str)(res)
            numeroBinario+=(str)(numeroDecimal)
            lista=list(numeroBinario)
            lista.reverse()
            print("Número binario obtenido: ",lista)
            break

          elif opcion == 'D' or opcion == 'd':
              numero = int(input("Ingrese un número en binario"))
              y = numero
              sumb = 0
              i = 0
              binario = numero
              while (i < y):
                  ultimonumero = binario % 10
                  binario = int(binario / 10)
                  if (ultimonumero == 0 or ultimonumero == 1):
                      sumb = sumb + 2 ** i * ultimonumero

                  i = i + 1
              lista=list(str(sumb))
              lista.reverse()
              print("El numero Binario es:", lista)
              break

          else:
           print("Usted a seleccionado un valor incorrecto porfavor verifique, gracias. ")
           break
    break