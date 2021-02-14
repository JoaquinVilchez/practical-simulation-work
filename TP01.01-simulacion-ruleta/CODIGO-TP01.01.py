
import random
import numpy as np
import matplotlib.pyplot as plt

n = 1000

def generaNumeros(tiradas):
   resultados = []
   for i in range(tiradas):
      resultados.append(random.randrange(37))
   return resultados

def mostrarFrecuenciaRelativa(lista):
   lista_frelat=[]
   for i in range(37):
      cant_nrorep = lista.count(i)/n
      lista_frelat.append(cant_nrorep)
   
   plt.plot(lista_frelat)

def mostrarVarianza(lista, varianza_esperada):
   lista_numeros=[]
   lista_vari=[]
   for i in lista:
      lista_numeros.append(i)
      lista_vari.append(np.var(lista_numeros))
   print(lista_vari,'\n')

   plt.axhline(varianza_esperada, color='red')
   plt.plot(lista_vari)


def mostrarMedia(lista, media_esperada):
   prom=[]
   acumi = 0
   pos=1

   for i in lista:
      acumi += i
      prom.append(acumi/pos)
      pos+=1
   
   plt.axhline(media_esperada, color='red')
   plt.plot(prom)
    

def mostrarDesvio(lista, desvio_esperado):

  numerosSum =[]
  desvios =[]
  tiradas = []
  for i, numero in enumerate(lista, start=1):   
    numerosSum.append(numero)
    des = np.square(np.var(numerosSum))
    tiradas.append(i)
    desvios.append(des)
    
  plt.axhline(desvio_esperado, color='r', linestyle='-')
  plt.plot(tiradas,desvios)


#Programa
resultados_obtenidos = generaNumeros(n)

varianza_esperada = np.var(resultados_obtenidos)
media_esperada = np.mean(resultados_obtenidos)
desvio_esperado = np.square(varianza_esperada)

mostrarFrecuenciaRelativa(resultados_obtenidos)
plt.title("Frecuencias relativas")
plt.xlabel("Numeros obtenidos")
plt.ylabel("Frecuencia")
plt.show()
mostrarVarianza(resultados_obtenidos, varianza_esperada)
plt.title("Tabla de varianzas ")
plt.xlabel("Numeros obtenidos")
plt.ylabel("Varianza")
plt.show()
mostrarMedia(resultados_obtenidos, media_esperada)
plt.title('Promedio Media ')
plt.xlabel('Tiradas')
plt.ylabel('Promedio Media')
plt.show()
mostrarDesvio(resultados_obtenidos, desvio_esperado)
plt.title("Desvío del número obtenido")
plt.xlabel("Número de tiradas")
plt.ylabel("Desvío")
plt.show()

# #Repetir
resultados = []

for i in range(6):
   resultados.append(generaNumeros(n))

varianza_esperada = np.var(resultados)
media_esperada = np.mean(resultados)
desvio_esperado = np.square(varianza_esperada)

# frecuencias
for i in range(len(resultados)):
   mostrarFrecuenciaRelativa(resultados[i])
plt.title("Frecuencias relativas en 5 tiradas")
plt.xlabel("Numeros obtenidos")
plt.ylabel("Frecuencia")
plt.show()

# varianza
for i in range(len(resultados)):
   mostrarVarianza(resultados[i], varianza_esperada)
plt.title("Varianzas en 5 tiradas")
plt.xlabel("Numeros obtenidos")
plt.ylabel("Varianza")
plt.show()

# media
for i in range(len(resultados)):
   mostrarMedia(resultados[i], media_esperada)
plt.title('Promedio Media en 5 tiradas')
plt.xlabel('Tiradas')
plt.ylabel('Promedio Media')
plt.show()

# desvio
for i in range(len(resultados)):
   mostrarDesvio(resultados[i], desvio_esperado)
plt.title("Desvío del número obtenido en 5 tiradas")
plt.xlabel("Número de tiradas")
plt.ylabel("Desvío")
plt.show()



