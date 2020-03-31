import numpy
m = int(input("Masukkan batas baris [m] : "))
n = int(input("Masukkan batas kolom  [n] : "))
matrix = numpy.zeros((m,n))
x = numpy.zeros((m))

vector = numpy.zeros((n))
comp = numpy.zeros((m))
error = []

print("Metode Iterasi Gauss Seidel")
for r in range (0, m):
    for c in range (0, n):
        matrix[(r),(c)] = float(input("Elemen a["+str(r+1)+str(c+1)+"] : "))
    vector[(r)] = float(input("b["+str(r+1)+"]: "))
tol = float(input("Masukkan toleransi error : "))
iterasi = int(input("Masukkan iterasi maksimum : "))
#Metode Gaus Seidel
k = 0
while k < iterasi:
    suma = 0
    k = k+1
    for r in range(0, m):
        suma=0
        for c in range(0, n):
            if(c != r):
                suma = suma+matrix[r,c]*x[c]
        x[r] = (vector[r]- suma)/matrix[r,r]
        print("x["+str(r)+"]: "+str(x[r]))
    del error[:]
    #Comprobation
    for r in range(0, m):
        suma=0
        for c in range(0, n):
            suma = suma+matrix[r,c]*x[c]
        comp[r] = suma
        dif = abs(comp[r]- vector[r])
        error.append(dif)
        print("Error en x[",r,"]=",error[r])
    print("Iterasi : ",k)
    if all(i <=tol for i in error) == True:
        break


