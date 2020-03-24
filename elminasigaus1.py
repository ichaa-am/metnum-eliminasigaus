import numpy as np 
A = np.array([[3, 4, 2],
             [1, 1, 2],
             [2, 1, 3]], float)
B = np.array([[34],
             [18],
             [26]], float)
AB = np.hstack([A, B])
print(AB)

n = len(B)
for p in range(0, n-1):
    for q in range(p + 1, n):
        lam= AB[p, p] / AB[q, p]
        AB[q] = AB[p] - lam * AB[q]
print("\nEliminasi Gauss:\n", AB)

for p in range(n-1, -1, -1):
    AB[p] = AB[p] / AB[p, p]
    for q in range(p - 1, -1, -1):
        lam = AB[p, p] / AB[q, p]
        AB[q] = AB[p] - lam * AB[q]
print("\nSubstitusi:\n", AB)

hasil = AB[:, 3]
print("\nHasil:\n[X, Y, Z]=",hasil)