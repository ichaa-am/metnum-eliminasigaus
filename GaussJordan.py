import numpy as np
n = int(input("masukkan ordo : "))
t = [[0 for i in range(n+1)] for j in range(n)]
for i in range (0,n):
    for j in range(0,n+1):
        t[i][j]=int(input(f"Masukkan bairs ke-{i+1}, kolom ke-{j+1} : "))
for i in t:
    for j in i:
        print(j,end=" |")
    print()


for i in range (0,n):
    if(t[i][i]!=1):
        for j in range (n,-1,-1):
            t[i][j]=np.divide(t[i][j],t[i][i])
    for k in range (i+1,n):
        for l in range (n,-1,-1):
            t[k][l]=t[k][l] - np.multiply(t[k][i],t[i][l])

print("\nHasil Gauss : ") 
for i in t:
    for j in i:
        print(j,end=" |")
    print()
    
for i in range(n-1,-1,-1):
    for k in range (i-1,-1,-1):
        for l in range (n,-1,-1):
            t[k][l]=t[k][l] - np.multiply(t[k][i],t[i][l])
    
print("\nHasil Gauss Jordan (untuk mencari nilai x) : ") 
for i in t:
    for j in i:
        print(j,end=" |")
    print()

x = [0 for i in range(n)]
for i in range (0,n):
    x[i] = t[i][n]

print("\nHasil Nilai x secara berurutan : ")
print(x)
print("\nHasil Error persamaan dengan memasukkan x ditemukan : ")
print(3*x[0]+4*x[1]+2*x[2])
print(x[0]+x[1]+2*x[2])
print(2*x[0]+x[1]+3*x[2])
