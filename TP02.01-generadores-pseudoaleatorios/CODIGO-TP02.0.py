import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats as ss


def mediaCuadrados():
    semillas = []
    numeros = []

    print('\nMETODO - MEDIA CUADRADOS')
    semilla = int(input('Ingrese un numero de cuatro digitos: '))
    tiradas = int(input('Ingrese cantidad de tiradas: '))
    for i in range(1, tiradas):
        numero = (semilla * semilla)
        semillas.append(numero)
        cantdigitos = (str(numero))

        while len(cantdigitos) < 8:
            cantdigitos= '0'+ cantdigitos

        semilla=int(cantdigitos[2:6])
        numeros.append(round((semilla/9999),4))

    print('\nRESULTADOS:\n',numeros, '\n')

    x = list(range(1, tiradas))
    y = numeros

    plt.scatter(x, y, label='Numeros aleatorios', color='k')
    plt.show()
    plt.plot(numeros)
    plt.show()


def multiplicativo():
    print('\nMETODO - MULTIPLICATIVO')
    semilla = int(input('Ingrese semilla:'))
    cmultiplicativa = int(input('Ingrese constante multiplicativa: '))
    modulo = int(input('Ingrese el modulo: '))
    tiradas = int(input('Ingrese cantidad de tiradas: '))
    numeros = []  
    for i in range(0, tiradas):
        numero = (cmultiplicativa * semilla) % modulo
        resultado = numero / (modulo - 1)
        semilla = numero
        numeros.append(resultado)
    
    print('\nRESULTADOS:\n',numeros,'\n')

    x=list(range(1,tiradas+1))
    y=numeros
    plt.scatter(x,y, label='Numeros aleatorios', color='k')
    plt.show()
    plt.plot(numeros)
    plt.show()

    print('\n============PRUEBA DE BONDAD===============')
    bondad(numeros,tiradas)
    print('\n============PRUEBA DE AUTOCORRELACION===============')
    autocorrelacion(numeros)    
    print('\n============PRUEBA DE POKER===============')
    poker(numeros)
    print('\n============PRUEBA DE LAS CORRIDAS===============')
    corridas(numeros,tiradas)

    
    
def lineal():
    print('\nMETODO - LINEAL')
    semilla = int(input('Ingrese semilla:'))
    cm = int(input('Ingrese constante multiplicativa: '))
    c = int(input('Ingrese incremento (nro impar): '))
    m = int(input('Ingrese el modulo: '))
    tiradas = int(input('Ingrese cantidad de tiradas: '))
    numeros = []
    for i in range(0, tiradas):
        numero = (cm * semilla + c) % m
        resultado = numero / (m - 1)
        semilla = numero
        numeros.append(resultado)
    print(numeros)

    x=list(range(1,tiradas+1))
    y=numeros
    plt.scatter(x,y, label='Numeros aleatorios', color='k')
    plt.show()
    plt.plot(numeros)
    plt.show()
#########################################################################

#CHI CUADRADO
def chicuadrado(oi,ei, grados_libertad):
    print('\n#### CHI CUADRADO ####')


    sumatoria = []

    for i in range(len(oi)):
        resultado = ((np.square(oi[i]-ei[i]))/ei[i])
        sumatoria.append(resultado)

    resultado_chi2=np.sum(sumatoria)

    print('RESULTADO DE CHI CUADRADO (z): ',resultado_chi2)

    tabla_chi2=ss.chi2.isf(0.05, grados_libertad)

    print('{0} < {1}'.format(resultado_chi2, tabla_chi2))
    if (resultado_chi2 < tabla_chi2):
        print('LOS NUMEROS SON INDEPENDIENTES.\n')
    else:
        print('LOS NUMEROS NO SON INDEPENDIENTES.\n')

    # print('Grados de libertad recibidos por parametro: ', grados_libertad)
    # print('Oi: ', oi)
    # print('Ei: ', ei)

    # chitest = ss.chisquare(oi,ei, grados_libertad)

    # print('RESULTADO CHI FUNCION: ', chitest)

    # significacion = (1-chitest.pvalue/100)

    # if chitest.pvalue < 0.01:
    #     print('NIVEL DE SIGNIFICACION: ', significacion,'%')
    #     print("NO SE AJUSTA A UNA NORMAL")
    # else:
    #     print('NIVEL DE SIGNIFICACION: ', significacion,'%')
    #     print("SE PUEDE AJUSTAR A UNA NORMAL")

#KOLMOGOROV-SMIRNOV
def kolmogorovSmirnov(numeros):
    print('\n#### KOLMOGOROV-SMIRNOV ####')
    media, desviacion = ss.norm.fit(numeros)

    kstest = ss.kstest(numeros,"norm",args=(media,desviacion))

    significacion = (1-kstest.pvalue/100)
    print('NIVEL DE SIGNIFICACION: ', significacion,'%')

    if kstest.pvalue < 0.01:
        print('LOS NUMEROS SON INDEPENDIENTES.\n')
    else:
        print('LOS NUMEROS NO SON INDEPENDIENTES.\n')

###############################################################################
#TEST DE BONDAD
def bondad(numeros, tiradas):
    print('TIRADAS: ', tiradas)
    m=int(np.sqrt(tiradas))
    print('M: ',m)
    
    intervalos=[]

    for i in range(m+1):
        intervalo=i/m
        intervalos.append(intervalo)

    division = pd.cut(numeros, bins=intervalos)
    
    oi = division.value_counts().reindex().tolist()
    ei = []

    for i in range(len(oi)):
        resultado = int(tiradas/m)
        ei.append(resultado)

    print('INTERVALOS: ', intervalos)
    print('FRECUENCIA OBSERVADA: ', oi)
    print('FRECUENCIA ESPERADA: ', ei)

    grados_libertad = m-1

    chicuadrado(oi,ei,grados_libertad)
    kolmogorovSmirnov(numeros)

###############################################################################
#TEST DE AUTOCORRELACION        
def autocorrelacion(numeros):
    error = float(input('Ingrese el margen de error: '))
    n = numeros
    i = int(input('Ingrese el primer numero donde empieza la amplitud de autocorrelacion: '))
    m = int(input('Ingrese amplitud de autocorrelacion: '))
    M = int(np.around((len(numeros)-i)/m-1))

    numeros_interes = []
    
    for x in range(M):
        j = i+(m*x)
        k = i+m*(x+1)
        resultado = numeros[j]*numeros[k]
        numeros_interes.append(resultado)        
    
    densidad_probabilidad = np.sum(numeros_interes)/(M+1)

    print('DENSIDAD DE PROBABILIDAD: ',densidad_probabilidad)

    desviacion_estandar = np.sqrt((13*M)+7)/(12*(M+1))

    print('DESVIACION ESTANDAR: ',desviacion_estandar)

    significacion = (densidad_probabilidad - 0.25)/desviacion_estandar

    print('SIGNIFICACION: ',significacion)

    z = (1-error)/2

    print('Z: ', z)

    conclusion=significacion-z

    if(conclusion != 0):
        print('LOS NUMEROS SON INDEPENDIENTES.\n')
    else:
        print('LOS NUMEROS NO SON INDEPENDIENTES.\n')
    
#TEST DE POKER
def poker(numeros):
    lista = []
    TD=0
    P1=0
    P2=0
    TP=0
    T=0
    P=0
    Q=0

    for i in numeros:
        resultado = np.around(i,5)
        lista.append(resultado)

    for i in lista:
        numero=i
        decimal = str(numero-int(numero))[2:].zfill(5)
        
        A=None
        B=None
        C=None
        D=None
        E=None
        
        decimal_resultado = []
        counter = 0
        for j in decimal:
            counter = counter+1
            if counter <= 5:
                if (A!=None):
                    if(j==A):
                        decimal_resultado.append('A')
                        continue
                else:
                    A=j
                    decimal_resultado.append('A')
                    continue
                
                if (B!=None):
                    if(j==B):
                        decimal_resultado.append('B')
                        continue
                else:
                    B=j
                    decimal_resultado.append('B')
                    continue

                if (C!=None):
                    if(j==C):
                        decimal_resultado.append('C')
                        continue
                else:
                    C=j
                    decimal_resultado.append('C')
                    continue

                if (D!=None):
                    if(j==D):
                        decimal_resultado.append('D')
                        continue
                else:
                    D=j
                    decimal_resultado.append('D')
                    continue

                if (E!=None):
                    if(j==E):
                        decimal_resultado.append('E')
                        continue
                else:
                    E=j
                    decimal_resultado.append('E')
                    continue
        
        cant_A = 0
        cant_B = 0
        cant_C = 0
        cant_D = 0
        cant_E = 0

        for x in decimal_resultado:
            if(x=='A'):
                cant_A = cant_A+1
            elif(x=='B'):
                cant_B = cant_B+1
            elif(x=='C'):
                cant_C = cant_C+1
            elif(x=='D'):
                cant_D = cant_D+1
            elif(x=='E'):
                cant_E = cant_E+1

        frecuencia = [cant_A,cant_B,cant_C,cant_D,cant_E]        

        frecuencia.sort(reverse=True)

        
        if(frecuencia==[1,1,1,1,1]):
            #TODOS DISTINTOS
            TD = TD+1
        elif(frecuencia==[2,1,1,1,0]):
            #PAR
            P1 = P1+1
        elif(frecuencia==[2,2,1,0,0]):
            #2 PARES
            P2 = P2+1
        elif(frecuencia==[3,1,1,0,0]):
            #TERCIA
            T = T+1
        elif(frecuencia==[3,2,0,0,0]):
            #TERCIA Y PAR
            TP = TP+1
        elif(frecuencia==[4,1,0,0,0]):
            #POKER
            P = P+1
        elif(frecuencia==[5,0,0,0,0]):
            #QUINTINA
            Q = Q+1        
    
    probabilidades = [0.3025,0.504,0.108,0.009,0.072,0.0045,0.0001]
    ei=[]

    for i in probabilidades:
        resultado = i*100
        ei.append(np.round(resultado,2))
        
    oi = [TD,P1,P2,T,TP,P,Q]
    print('Ei: ', ei)
    print('Oi: ', oi)

    grados_libertad = int(input('Ingrese grados de libertad: '))
    chicuadrado(oi, ei, grados_libertad)

#PRUEBA CORRIDAS
def corridas(numeros, tiradas):
    bit = []
    numero_de_corridas = -1
    for i in range(1, len(numeros)):
        if numeros [i] <= numeros[i - 1]:
            bit.append(0)
        else:
             bit.append(1)
        if i == 1:
            numero_de_corridas = 1
        else:
            if bit[i - 1] != bit[i - 2]:
                numero_de_corridas += 1
    print('El resultado es', bit)
    print('El numero de corridas es', numero_de_corridas)
    media = ((2 * tiradas) - 1) / 3
    varianza = ((16 * tiradas) - 29) / 90
    estadistico = (numero_de_corridas - media) / varianza
    print('El valor esperado es', media)
    print('La varianza es', varianza)
    print('El valor de Z es', estadistico)
    print('Significacion de 0.05')#en tabla 1.96
    v2 = ss.norm()
    v3 = ss.norm()
    rv2 = v2.cdf(1.96)
    rv3 = v3.cdf(estadistico)
    if (abs (rv3) <= rv2):
         print('LOS NUMEROS SON INDEPENDIENTES')
    else:
         print('LOS NUMEROS NO SON INDEPENDIENTES')

#PROGRAMA:

mediaCuadrados()
multiplicativo()
lineal()

