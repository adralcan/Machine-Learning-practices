
# coding: utf-8

# In[101]:


import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


# In[161]:


def createFunction(fun, a, b):
    M = np.arange(a, b, 0.01)
    Y = fun(M)
    plt.plot(M, Y)
    #Devolvemos los puntos de la función para calcular los puntos que quedan por encima/debajo de ella
    return M, Y;

def createPoints(fun, a, b, M, Y):
        #Ajustamos la altura de la representación de los puntos en Y para que no se salgan de los valores de la gráfica
        alt = max(fun(M))
        size = len(M)
        plt.xlim(a-0.1, b+0.1) 
        plt.ylim(-0.1, alt+0.1)
        y = np.random.uniform(low=0.0, high=alt, size=(size))     
        valor = monteCarlo(fun, M, Y, y, size)   
        plt.plot(M, y, 'x')       
        return valor;
    
def monteCarlo(fun, M, Y, y, size):  
    correctos = np.sum(Y < y)
    return(correctos*100)/size


# In[162]:


#No hace falta el for que había antes, el método createPoints los pinta todos en el rango que le damos
def integra_mc(fun, a, b, num_puntos=10000):
        M, Y = createFunction(fun, a, b)  
        valor = createPoints(fun, a, b, M, Y)

        print("Porcentaje: " + str(valor))
        plt.show()
      


# In[167]:


integra_mc(np.sin, 0, np.pi)

