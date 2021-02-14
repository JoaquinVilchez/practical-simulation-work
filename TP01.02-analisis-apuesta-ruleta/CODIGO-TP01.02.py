import numpy as np
import random
import matplotlib.pyplot as plt

rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
columna1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
columna2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
columna3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

n = 1000 # tiradas infinitas
r = 5 # repeticiones del programa

# PLENO - OK
def pleno(capital, numero, monto):
    # global capital
    lista_capital = []
    resultados=[]
    tiradas = 0

    if capital is False: #SI EL CAPITAL ES INFINITO

        for i in range(n):
            resultado = random.randrange(37)
            resultados.append(resultado)
            print('==================')
            print("Salio el numero: ", resultado)
            if resultado == numero:
                ganancia = monto*36
                capital = capital+ganancia
                print('Felicitaciones, Gano $', ganancia, '!')
                print('==================')
                lista_capital.append(capital)
            else:
                capital = capital - monto
                print('Ha perdido $', monto)
                print('==================')
                lista_capital.append(capital)

        plt.plot(lista_capital)

        if(repeat==False):            
            plt.show()

            lista_fabsol = []
            lista_frelat = []
            cant_nror = 0
            for x in range(0,n):
                cant_nror = resultados.count(x)
                lista_fabsol.append(cant_nror)
                cant_nror = resultados.count(x)/n
                lista_frelat.append(cant_nror)
            plt.hist(resultados, bins=37, alpha=1, edgecolor = 'green', linewidth=1.2,color = 'yellow')
            plt.title('HISTOGRAMA')
            plt.xlabel('Valores de la ruleta')
            plt.ylabel('Frecuencia absoluta')
            plt.show()

    else: #SI EL CAPITAL ES REAL
        plt.axhline(capital)

        while capital >= monto and tiradas<=n:
            tiradas = tiradas+1
            resultado = random.randrange(37)
            resultados.append(resultado)
            print('==================')
            print("Salio el numero: ", resultado)
            if resultado == numero:
                ganancia = monto*36
                capital = capital+ganancia
                print('Felicitaciones, Gano $', ganancia, '!')
                print('SU BANCA ES DE: $', capital)
                print('==================')
                lista_capital.append(capital)
            else:
                capital = capital-monto
                print('Ha perdido $', monto)
                print('SU BANCA ES DE: $', capital)
                print('==================')
                lista_capital.append(capital)
        
        if tiradas == n:
            print("Se cumplieron las ", n, " tiradas.")
        else:
            print("Se quedo sin dinero.")

        plt.plot(lista_capital)

        if(repeat==False):            
            plt.show()

            lista_fabsol = []
            lista_frelat = []
            cant_nror = 0
            for x in range(0,tiradas):
                cant_nror = resultados.count(x)
                lista_fabsol.append(cant_nror)
                cant_nror = resultados.count(x)/tiradas
                lista_frelat.append(cant_nror)
            plt.hist(resultados, bins=37, alpha=1, edgecolor = 'green', linewidth=1.2,color = 'yellow')
            plt.title('HISTOGRAMA')
            plt.xlabel('Valores de la ruleta')
            plt.ylabel('Frecuencia absoluta')
            plt.show()
#FIN PLENO

# COLOR
def color(capital, eleccion, monto):
    lista_capital = []
    resultados=[]
    tiradas = 0

    if capital is False: #SI EL CAPITAL ES INFINITO

        for i in range(n):
            resultado = random.randrange(37)
            resultados.append(resultado)

            for x in range(len(rojos)):
                if resultado == rojos[x]:
                    resultado_color = 1 #ES ROJO
                    nombre_color = "Rojo"
                    break

            for x in range(len(negros)):
                if resultado == negros[x]:
                    resultado_color = 2 #ES NEGRO
                    nombre_color = "Negro"
                    break

            print('==================')
            print("Salio el numero: ", resultado, " - ", nombre_color)
            

            if resultado_color == eleccion:
                ganancia = monto*2
                capital = capital+ganancia
                print('Felicitaciones, Gano $', ganancia, '!')
                print('SU BANCA ES DE: $', capital)
                print('=========================')
                lista_capital.append(capital)
            else:
                capital = capital - monto
                print('Ha perdido $', monto)
                print('SU BANCA ES DE: $', capital)
                print('=========================')
                lista_capital.append(capital)

        plt.plot(lista_capital)

        if(repeat==False):            
            plt.show()

            lista_fabsol = []
            lista_frelat = []
            cant_nror = 0
            for x in range(0,n):
                cant_nror = resultados.count(x)
                lista_fabsol.append(cant_nror)
                cant_nror = resultados.count(x)/n
                lista_frelat.append(cant_nror)
            plt.hist(resultados, bins=37, alpha=1, edgecolor = 'green', linewidth=1.2,color = 'yellow')
            plt.title('HISTOGRAMA')
            plt.xlabel('Valores de la ruleta')
            plt.ylabel('Frecuencia absoluta')
            plt.show()

    else:
        plt.axhline(capital)
        while capital >= monto and tiradas<=n:
            tiradas = tiradas+1
            resultado = random.randrange(37)
            resultados.append(resultado)

            for x in range(len(rojos)):
                if resultado == rojos[x]:
                    resultado_color = 1 #SALIO ROJO
                    nombre_color = "Rojo"
                    break

            for x in range(len(negros)):
                if resultado == negros[x]:
                    resultado_color = 2 #SALIO NEGRO
                    nombre_color = "Negro"
                    break

            print('=========================')
            print("Salio el numero: ", resultado, " - ",nombre_color)


            if resultado_color == eleccion:
                ganancia = monto*2
                capital = capital+ganancia
                print('Felicitaciones, Gano $', ganancia, '!')
                print('SU BANCA ES DE: $', capital)
                print('=========================')
                lista_capital.append(capital)
            else:
                capital = capital - monto
                print('Ha perdido $', monto)
                print('SU BANCA ES DE: $', capital)
                print('=========================')
                lista_capital.append(capital)


        print("Se completaron las ", n, "tiradas")

        plt.plot(lista_capital)

        if(repeat==False):            
            plt.show()

            lista_fabsol = []
            lista_frelat = []
            cant_nror = 0
            for x in range(0,tiradas):
                cant_nror = resultados.count(x)
                lista_fabsol.append(cant_nror)
                cant_nror = resultados.count(x)/tiradas
                lista_frelat.append(cant_nror)
            plt.hist(resultados, bins=37, alpha=1, edgecolor = 'green', linewidth=1.2,color = 'yellow')
            plt.title('HISTOGRAMA')
            plt.xlabel('Valores de la ruleta')
            plt.ylabel('Frecuencia absoluta')
            plt.show()
# FIN COLOR

#COLUMNA
def columna(capital, eleccion, monto):
    lista_capital = []
    resultados=[]
    tiradas = 0

    if capital is False: #SI EL CAPITAL ES INFINITO
        for i in range(n):
            resultado = random.randrange(37)
            resultados.append(resultado)

            for x in range(len(columna1)):
                if resultado == columna1[x]:
                    resultado_columna = 1 #ES DE LA COLUMNA 1
                    break

            
            for x in range(len(columna2)):
                if resultado == columna2[x]:
                    resultado_columna = 2 #ES DE LA COLUMNA 2
                    break

            
            for x in range(len(columna3)):
                if resultado == columna3[x]:
                    resultado_columna = 3 #ES DE LA COLUMNA 3
                    break

            # print('=========================')
            # print("Salio el numero: ", resultado, " - Columna: ", resultado_columna)

            if resultado_columna == eleccion:
                ganancia = monto*3
                capital = capital+ganancia
                print('Felicitaciones, Gano $', ganancia, '!')
                print('SU BANCA ES DE: $', capital)
                print('=========================')
                lista_capital.append(capital)
            else:
                capital = capital-monto
                print('Ha perdido $', monto)
                print('SU BANCA ES DE: $', capital)
                print('=========================')
                lista_capital.append(capital)

        plt.plot(lista_capital)

        if(repeat==False):            
            plt.show()

            lista_fabsol = []
            lista_frelat = []
            cant_nror = 0
            for x in range(0,n):
                cant_nror = resultados.count(x)
                lista_fabsol.append(cant_nror)
                cant_nror = resultados.count(x)/n
                lista_frelat.append(cant_nror)
            plt.hist(resultados, bins=37, alpha=1, edgecolor = 'green', linewidth=1.2,color = 'yellow')
            plt.title('HISTOGRAMA')
            plt.xlabel('Valores de la ruleta')
            plt.ylabel('Frecuencia absoluta')
            plt.show()

    else:
        plt.axhline(capital)
        while capital >= monto and tiradas<=n:
            tiradas = tiradas+1
            resultado = random.randrange(37)
            resultados.append(resultado)

            for x in range(len(columna1)):
                if resultado == columna1[x]:
                    resultado_columna = 1 #ES DE LA COLUMNA 1
                    break

            for x in range(len(columna2)):
                if resultado == columna2[x]:
                    resultado_columna = 2 #ES DE LA COLUMNA 2
                    break

            for x in range(len(columna3)):
                if resultado == columna3[x]:
                    resultado_columna = 3 #ES DE LA COLUMNA 3
                    break
            # print('=========================')
            # print("Salio el numero: ", resultado, " - Columna: ", resultado_columna)

            if resultado_columna == eleccion:
                ganancia = monto*3
                capital = capital+ganancia
                print('Felicitaciones, Gano $', ganancia, '!')
                print('SU BANCA ES DE: $', capital)
                print('=========================')
                lista_capital.append(capital)
            else:
                capital = capital - monto
                print('Ha perdido $', monto)
                print('SU BANCA ES DE: $', capital)
                print('=========================')
                lista_capital.append(capital)

        print("Se quedo sin dinero.")
        
        plt.plot(lista_capital)

        if(repeat==False):            
            plt.show()

            lista_fabsol = []
            lista_frelat = []
            cant_nror = 0
            for x in range(0,tiradas):
                cant_nror = resultados.count(x)
                lista_fabsol.append(cant_nror)
                cant_nror = resultados.count(x)/tiradas
                lista_frelat.append(cant_nror)
            plt.hist(resultados, bins=37, alpha=1, edgecolor = 'green', linewidth=1.2,color = 'yellow')
            plt.title('HISTOGRAMA')
            plt.xlabel('Valores de la ruleta')
            plt.ylabel('Frecuencia absoluta')
            plt.show()
#FIN COLUMNA

# MARTINGALA
def martingala(capital, eleccion, monto):
    lista_capital = []
    resultados=[]
    tiradas = 0
    fichas = 1

    if capital is False: #SI EL CAPITAL ES INFINITO

        for i in range(n):
            print('==================')
            print("USTED APUESTA: ", fichas, " FICHAS = $",(fichas*monto))
            resultado = random.randrange(37)
            resultados.append(resultado)

            for x in range(len(rojos)):
                if resultado == rojos[x]:
                    resultado_color = 1 #ES ROJO
                    nombre_color = "Rojo"
                    break

            for x in range(len(negros)):
                if resultado == negros[x]:
                    resultado_color = 2 #ES NEGRO
                    nombre_color = "Negro"
                    break

            print("Salio el numero: ", resultado, " - ",nombre_color)

            if resultado_color == eleccion: #SI GANA
                ganancia = (monto*fichas)*2
                capital = capital+ganancia
                print('Felicitaciones, Gano $', ganancia, '!')
                print('SU BANCA ES DE: ', capital)
                print('==================')
                lista_capital.append(capital)
                fichas = 1
            else: #SI PIERDE
                capital = capital - (monto*fichas)
                print('Ha perdido $', monto)
                print('SU BANCA ES DE: $', capital)
                print('==================')
                lista_capital.append(capital)                
                fichas = fichas * 2

        plt.plot(lista_capital)

        if(repeat==False):            
            plt.show()

    else:
        plt.axhline(capital)
        while capital >= (monto*fichas) and tiradas<=n:
            print('==================')
            print("USTED APUESTA: ", fichas, " FICHAS = $",(fichas*monto))
            tiradas = tiradas+1
            resultado = random.randrange(37)
            resultados.append(resultado)

            for x in range(len(rojos)):
                if resultado == rojos[x]:
                    resultado_color = 1 #SALIO ROJO
                    nombre_color = "Rojo"
                    break

            for x in range(len(negros)):
                if resultado == negros[x]:
                    resultado_color = 2 #SALIO NEGRO
                    nombre_color = "Negro"
                    break

            print("Salio el numero: ", resultado, " - ",nombre_color)


            if resultado_color == eleccion:
                ganancia = monto*2
                capital = capital+ganancia
                print('Felicitaciones, Gano $', ganancia, '!')
                print('SU BANCA ES DE: $', capital)
                lista_capital.append(capital)
                fichas = 1
            else:
                capital = capital - monto
                print('Ha perdido $', monto)
                print('SU BANCA ES DE: $', capital)
                lista_capital.append(capital)
                fichas = fichas * 2
                
                while capital <= (monto*fichas):
                    fichas = fichas-1
                    if fichas==0:
                        break

        if tiradas==n:
            print("Se cumplieron las ", n, " tiradas.")
        else:
            print("Se quedo sin dinero.")


        plt.plot(lista_capital)

        if(repeat==False):            
            plt.show()

            lista_fabsol = []
            lista_frelat = []
            cant_nror = 0
            for x in range(0,tiradas):
                cant_nror = resultados.count(x)
                lista_fabsol.append(cant_nror)
                cant_nror = resultados.count(x)/tiradas
                lista_frelat.append(cant_nror)
            plt.hist(resultados, bins=37, alpha=1, edgecolor = 'green', linewidth=1.2,color = 'yellow')
            plt.title('HISTOGRAMA')
            plt.xlabel('Valores de la ruleta')
            plt.ylabel('Frecuencia absoluta')
            plt.show()
# FIN MARTINGALA

# PROGRAMA PRINCIPAL
print("Bienvenido a la ruleta, su banca es $0, para poder empezar a jugar debe ingresar dinero.\nEn caso que desee tener una banca infinita, presione 0")
dinero = int(input('Ingrese el capital inicial:'))
repeat=False

if dinero != 0:
    print("\nSu banca es de $", dinero, "\n")
else:
    print("\nSu banca es infinita\n")
    dinero = False

print("Empieza el juego: \n")
print('Elija metodo de apuesta:')
print('1 - Pleno')
print('2 - Color')
print('3 - Columna')
print('4 - Martingala\n')

opcion = int(input('Opción:'))

if opcion == 1:
    print("====PLENO====")
    numero = int(input('Elija un numero: '))
    monto = int(input('Cuanto dinero apuesta? $'))
    pleno(dinero, numero, monto)
elif opcion == 2:
    print("====COLOR====")
    eleccion = int(input('Elija un color: \n 1.Rojo\n 2.Negro\n'))
    monto = int(input('Cuanto dinero apuesta? $'))
    color(dinero, eleccion, monto)
elif opcion == 3:
    print("====COLUMNA====")
    print('Elija una columna: \n')
    print('1. :', columna1)
    print('2. :', columna2)
    print('3. :', columna3)
    eleccion = int(input('Elija una opcion: \n'))
    monto = int(input('Cuanto dinero apuesta? $'))
    columna(dinero, eleccion, monto)
elif opcion == 4:
    print("====MARTINGALA====")
    eleccion = int(input('Elija un color: \n 1.Rojo\n 2.Negro\n'))
    monto = int(input('Cuanto dinero apuesta? $'))
    martingala(dinero, eleccion, monto)
#FIN PROGRAMA PRICIPAL


#PROGRAMA REPETIDO VARIAS VECES

print("Bienvenido a la ruleta, su banca es $0, para poder empezar a jugar debe ingresar dinero.\nEn caso que desee tener una banca infinita, presione 0")
dinero = int(input('Ingrese el capital inicial:'))

if dinero != 0:
    print("\nSu banca es de $", dinero, "\n")
else:
    print("\nSu banca es infinita\n")
    dinero = False

print("Empieza el juego: \n")
print('Elija metodo de apuesta:')
print('1 - Pleno')
print('2 - Color')
print('3 - Columna')
print('4 - Martingala\n')

opcion = int(input('Opción:'))

if opcion == 1:
    print("====PLENO====")
    numero = int(input('Elija un numero: '))
    monto = int(input('Cuanto dinero apuesta? $'))
    for i in range(r):
        repeat=True
        pleno(dinero, numero, monto)
elif opcion == 2:
    print("====COLOR====")
    eleccion = int(input('Elija un color: \n 1.Rojo\n 2.Negro\n'))
    monto = int(input('Cuanto dinero apuesta? $'))
    for i in range(r):
        repeat=True
        color(dinero, eleccion, monto)
elif opcion == 3:
    print("====COLUMNA====")
    print('Elija una columna: \n')
    print('1. :', columna1)
    print('2. :', columna2)
    print('3. :', columna3)
    eleccion = int(input('Elija una opcion: \n'))
    monto = int(input('Cuanto dinero apuesta? $'))
    for i in range(r):
        repeat=True
        columna(dinero, eleccion, monto)
elif opcion == 4:
    print("====MARTINGALA====")
    eleccion = int(input('Elija un color: \n 1.Rojo\n 2.Negro\n'))
    monto = int(input('Cuanto dinero apuesta? $'))
    for i in range(r):
        repeat=True
        martingala(dinero, eleccion, monto)
if repeat==True:
    plt.show()