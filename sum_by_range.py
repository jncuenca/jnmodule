"""
Suma todos los números en un rango
Pasamos una matriz de dos números. Devuelve la suma de esos dos números más la suma de todos los números entre ellos. 
El número más bajo no siempre vendrá primero.
Por ejemplo, sumAll([4,1]) debería devolver 10 porque la suma de todos los números entre 1 y 4 (ambos inclusive) es 10.
"""

def sum_all(arr):
  if arr[0] == arr[-1]:
    return 1
  
  new_arr = [arr[0], arr[-1]-1]
  return sum_all(new_arr) + arr[-1]

print(sum_all(sorted([4, 1])))
