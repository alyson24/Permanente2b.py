números = {10000, 20000, 50000, 70000, 100000, 150000} 
import time
import random

def INSERTION_SORT(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and key < A[i]:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

n = 10000
lista = list(range(n))
random.shuffle(lista)

t_inicio = time.time()
l = INSERTION_SORT(lista)
t_final = time.time()
tiempo = t_final - t_inicio
print(tiempo)
print(f"Tiempo de ejecución de un Insertion Sort para un n = {n} fue de:",tiempo)


def BUBBLESORT(L):
    n = len(L)
    for i in range(0, n):
        for j in range(n-1, i, -1):
            if L[j] < L[j-1]:
                key = L[j]
                L[j] = L[j-1]
                L[j-1] = key
                
    return L
  
n = 10000
lista = list(range(n))
random.shuffle(lista)
t1 = time.time()
l = BUBBLESORT(lista)
t2 = time.time()
t_final = t2-t1

print(t_final)
print(f"Tiempo de ejecución de un Bubble Sort para un n = {n} fue de:",t_final)
