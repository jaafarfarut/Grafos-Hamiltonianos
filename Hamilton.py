# se formara una matriz de adyacencia la cual se relaciona con un grafo no dirigido
# y sin bucles
matriz = []
# Para que se forme una matriz de adyacencia el numero de filas y columnas deben ser
# iguales
filas=input("ingrese el numero de filas: ")
columnas=input("ingrese el numero de columnas: ")
# declaramos una variable a
a=1
# Usamos la condicinal para cuando el numero en la fila y en la columna sean iguales
# el valor sea 0
if(filas==columnas):
   for i in range (filas):
       matriz.append([0]*columnas)
#En una matriz de adyacencia solo puede haber 0 y 1
   for f in range(filas):
       for c in range(columnas):
# le damos una forma mas cercana a una matriz empezando desde el 1 y no desde el 0 usando
# %(f+1,c+1)
              matriz[f][c]=input("Elemento %d,%d: " %(f+1,c+1))
# le damos el siguiente condicinal ya que las matrices de adyacencia de grafos no
# dirigidos tiene como valores sono 0 y 1, por lo tanto cualquier otro valor no se tendra
# en cuenta
   if(matriz[f][c]==1 or matriz[f][c]==0):
     for f in range(filas):
       if(a==1):
         for c in range(columnas):
            if(matriz[f][c]==matriz[c][f]):
                a=1
       elif(matriz[f][c]!=matriz[c][f]):
             a=0
   if(a==1):
      for f in range(filas):
         if(a==1):
           for c in range(columnas):
              if(f==c and matriz[f][c]==0):
                 a=1
              elif(f==c and matriz[f][c]!=0):
                 a=0
      if(a==1):
          print matriz
          print("es una matriz de adyacencia")
      elif(a!=1):
          print matriz
          print("no es una matriz de adyacencia")
   elif(a!=1):
        print matriz
        print("no es una matriz de adyacencia")
# hemos visto que la variable "a" es una condicional que nos permitio contruir para
# el problema cuando es igual o diferente de 1
   else:
       print("No se podra formar una matriz de adyacencia con esos valores")
else:
    print("No se podra formar una matriz de adyacencia")
