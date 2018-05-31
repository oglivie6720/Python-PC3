print("\t\t\t\t\t\t\t\tPrograma que te permite transformar de decimal a binario y viceversa.")


numeroDecimal=0
numeroBinario=""
res=0

opcion = input("Si desea transformar a binario toque b o B, si desea transformar a decimal toque d o D:   ")
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

      else:
          print("Hola a Todos")
          break