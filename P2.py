# -*- coding: utf-8 -*-

#Importamos las librerías con las que vamos a trabajar:
import sympy as sp
import numpy as np
from matplotlib import pyplot as plt 

#Escribimos la función recursiva "Factorial" necesaria para construir nuestros polinomios de Taylor.
def Factorial(entero): 
    if entero > 1:
        return(entero * Factorial(entero - 1))
    return 1


'''EJERCICIO 1'''
#Apartado 1) Calcular los 3 primeros polinomios de Taylor para la función f(x) = sen(x) en x = 0
print("---------------------------")
print("EJERCICIO 1:")
print("---------------------------")

#Declaramos gracias a la función symbols a x como un símbolo
x = sp.symbols('x')

#Declaramos nuestra función y x0:
f = sp.sin(x)
x0 = 0

#Construimos los polinomios de Taylor:
a0 = f.subs(x, x0)
a1 = sp.diff(f, x).subs(x, x0)
a2 = sp.diff(f, x, 2).subs(x, x0) / Factorial(2)
a3 = sp.diff(f, x, 3).subs(x, x0) / Factorial(3)

P0 = a0
P1 = a1*(x-x0)
P2 = a2*(x-x0)**2
P3 = a3*(x-x0)**3

#Construimos nuestro polinomio con el cual vamos a trabajar a partir de los polinomios anteriores
P = P0 + P1 + P2 + P3
print("P0 = ", P0)
print("P1 = ", P1)
print("P2 = ", P2)
print("P3 = ", P3)
print("Por tanto, muestro polinomio de Taylor será: ", P)


#Escribimos las funciones para posteriormente dibujarlas con Pyplot (las escribimos en y ya que x lo estamos usando como símbolo)
def f1(y):
    return -y**3/6 + y

def f2(y):
    return np.sin(y)

y = np.arange(-10, 10, 0.1)

plt.plot(y, [f1(i) for i in y])
plt.plot(y, [f2(i) for i in y])

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.xlim(-4, 4)
plt.ylim(-4, 4)

plt.legend(["f(x) = sen(x)", "P"])

plt.show()
    


'''EJERCICIO 2'''
#2. Escribir un procedimiento en python para hallar un valor aproximado de una función f en un punto z a partir de una lista de nodos

#La función a construir requiere como parámetros de entrada la función , un punto z y una lista de nodos (lista_xi)
def polinomioInterpolador(f, z, lista_xi):
    #Declaramos la lista donde vamos a guardar los valores de la función en los nodos;
    lista_fi = []
    #LLenamos la lista;
    for i in range(0, len(lista_xi)):
        lista_fi.append(f.subs(x, lista_xi[i]))
        
    #Creamos el polinomio interpolador:
    P_interpoladorParticular = 0
    P_interpoladorGeneral = 0
    L = []
    Li = []
    for i in range(0, len(lista_xi)):
        li = 1
        lx = 1
        for j in range(0, len(lista_xi)):
            if (j != i):
                li *= (z-lista_xi[j])/(lista_xi[i]-lista_xi[j])
                lx *= (x-lista_xi[j])/(lista_xi[i]-lista_xi[j])
                
        L.append(li)
        Li.append(lx)
        P_interpoladorParticular += lista_fi[i]*L[i]
        P_interpoladorGeneral += lista_fi[i]*Li[i]
        
    print(f'Para la funcion {f} en los nodos {lista_xi}, Obtenemos el siguiente polinomio interpolador: \n{P_interpoladorGeneral}\n')
    print (f'Para z={z}, f(z) toma el valor {round(P_interpoladorParticular, 3)}')
    
    
print("\n---------------------------")
print("EJERCICIO 2:")
print("---------------------------")
        
polinomioInterpolador(1/x, 3, [2, 5/2, 4])
        
