import random
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as ss
#-----------------------------DISTRIBUCIONES CONTINUAS-----------------------------
def UNIFORM (a,b):
    x=[]
    for i in range(1000):
        r = round(random.random(), 4)
        x.append(a+(b-a)*r)
    return x

def EXPENT (alfa):
    ex = 1/ alfa
    x = []
    for i in range(1000):
        r = random.random()
        x += [-ex*(math.log(r))]
    return x

def GAMMA (k,a):
    x=[]
    for i in range(1, 1000):
        tr=1.0
        for j in range(1,k):
            r = random.random()
            tr=tr*r
        x.append(-(math.log10(tr))/a)
    return x

def NORMAL(mean,sd):
    lista_normal=[]
    for j in range(1000):
        sum=0
        for i in range(1, 12):
            r=random.random()
            sum=sum+r
        x=(sd*(sum-6))+mean
        lista_normal.append(x)
    return lista_normal
#--------------------------DISTRIBUCIONES DISCRETAS-----------------------
def PASCAL(k,q):
    nx = []
    for i in range(1000):
        tr = 1
        qr = math.log10(q)
        for j in range(k):
            r = random.random()
            tr *= r
        x = int(math.log10(tr)//qr)
        nx.append(x)
    return nx

def BINOMIAL (n,p):
    x=[]
    for i in range(1000):
        y=0
        for j in range(1,n):
            r = random.random()
            if (r-p) <0:
                y+=1.0
        x.append(y)
    return x

def POISSON(p):
    listado_poisson = []
    for i in range(1000):
        x = 0
        b = np.exp(-p)
        tr = 1
        r = np.random.rand()
        tr = tr * r

        while ((tr - b) >= 0):
            x = x + 1
            r = np.random.rand()
            tr = tr * r
        listado_poisson.append(x)

    return listado_poisson

def HIPERGEOMETRICA(tn, ns, p):
    listado_hipergeometrica=[]
    for i in range(1000):    
        p_variable=p
        tn_variable=tn
        x=0
        s=0

        for i in range(1,ns):
            r = np.random.rand()        
            if (r-p_variable<=0):
                s=1
                x=x+1
            else:
                s=0
            p_variable=(tn_variable*p_variable-s)/(tn_variable-1)
            tn_variable=tn_variable-1
        
        listado_hipergeometrica.append(p_variable)
    
    return listado_hipergeometrica

def EMPIRICA():
  lista_empirica=[]
  p=[0.273,0.037,0.195,0.009,0.124,0.058,0.062,0.151,0.047,0.044]
  for j in range (1000):
      r=random.random()
      a=0
      x=1
      for i in p:
        a+=i
        if (r<=a):
          break
        else:
          x=x+1
      lista_empirica.append(x)
  return lista_empirica


Uniforme=(UNIFORM(1,3))
Gamma=(GAMMA(3, 1))
Exponencial=(EXPENT(1))
Pascal=PASCAL(3,0.3)
Binomial = BINOMIAL (30, 0.4)
Poisson = POISSON(3.6)
Hipergeometrica = HIPERGEOMETRICA(10,5,0.4)
Normal=NORMAL(2.35,30)
Empirica=EMPIRICA()
def plotear(U, E, G, N, P, B, PS, H, EM):
    # distribuciones continuas
    # -------------Graficar uniforme---------------
    numerosUniformes = ss.uniform.rvs(size=1000, loc = 1, scale=3)
    sns.kdeplot(numerosUniformes, label="Distribución esperada")
    sns.distplot(U, hist_kws=dict(edgecolor="k"), label="Distribución observada")
    plt.title("Distribución Uniforme")
    plt.legend(loc="upper left")
    plt.show()

    # -------------Graficar Exponencial---------------
    numerosExponenciales=ss.expon.rvs(size=1000, loc=0, scale=1)
    sns.kdeplot(numerosExponenciales, label="Distribución esperada")
    sns.distplot(E, hist_kws=dict(edgecolor="k"), label="Distribución observada")
    plt.title("Distribución Exponencial")
    plt.legend(loc="upper left")
    plt.show()

    # -------------Graficar Gamma---------------
    plt.title("Distribución Gamma")
    plt.hist(G, alpha=1, edgecolor='black')
    plt.show()

    # -------------Graficar Normal---------------
    numerosNormales = ss.norm.rvs(size=1000, loc=2.35, scale=30)
    sns.kdeplot(numerosNormales, label="Distribución esperada")
    sns.distplot(N, hist_kws=dict(edgecolor="k"), label="Distribución observada")    
    plt.title("Distribución Normal")
    plt.legend(loc="upper left")
    plt.show()
    
    # distribuciones discretas

    # -------------Graficar Pascal---------------
    plt.title("Distribución Pascal")
    plt.hist(P, alpha=1, edgecolor='black')
    plt.show()

    #------------ Graficar binomial--------------
    N, p = 30, 0.4  # parametros de forma
    binomial = ss.binom(N, p)  # Distribución
    x = np.arange(binomial.ppf(0.01),
                  binomial.ppf(0.99))
    fmp = binomial.pmf(x)  # Función de Masa de Probabilidad
    plt.plot(x, fmp, '--' , label="Distribución esperada")
    sns.distplot(B,  hist_kws=dict(edgecolor="k"), label="Distribución observada")
    plt.title("Distribución Binomial")
    plt.ylabel('probabilidad')
    plt.xlabel('valores')
    plt.legend(loc="upper left")
    plt.show()

    # -------------Graficar Poisson---------------
    poisson = ss.poisson(3.6)
    xLine = np.arange(poisson.ppf(0.01),
                      poisson.ppf(0.99))
    fmp = poisson.pmf(xLine)
    plt.plot(xLine, fmp,  label="Distribución esperada")
    sns.distplot(PS, hist_kws=dict(edgecolor="k"), label="Distribución observada")
    plt.title("Distribución de Poisson")
    plt.legend(loc="upper left")
    plt.show()

    # -------------Graficar Hiper---------------
    plt.title("Distribución Hipergeometrica")
    plt.hist(H, alpha=1, edgecolor = 'black')
    plt.show()
    #-------------Graficar empirica------------
    sns.distplot(EM, hist_kws=dict(edgecolor="k"), label="Distribución observada")
    plt.title("Distribucion Empirica")
    plt.show()
    
plotear(Uniforme , Exponencial , Gamma , Normal, Pascal, Binomial, Poisson, Hipergeometrica, Empirica)
#---------------Test chi2 a la distribucion empirica---------
def TestChi2(emp):
    print("Test Chi Cuadrado para la distribucion Empírica")
    obs = []
    esp = []
    chi2tabla = round(ss.chi2.ppf(1 - 0.05, 9), 2)
    p = [0.273, 0.037, 0.195, 0.009, 0.124, 0.058, 0.062, 0.151, 0.047, 0.044]
    for i in range(10):
        x = 0
        for j in range(len(emp)):
            if emp[j]==i+1:
                x += 1
        obs.append(x)
        esp.append(1000 * p[i])
    chi2exp = 0
    n=len(obs)
    for i in range(n):
        x1 = (((obs[i]-esp[i])**2)/esp[i])
        chi2exp += x1

    print('χ2 experimento:', chi2exp)
    print('χ2 critico:', chi2tabla)
    if (chi2exp < chi2tabla):
        print("La muestra de datos pasa el test")
    else:
        print("La muestra de datos NO pasa el test")


TestChi2(Empirica)


