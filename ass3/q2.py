import numpy as np
from scipy.special import jv

# i)
N = 10**6
T = 10
print(N)
print(T)

# ii)
x = np.linspace(0, T, N + 1)
sx = x[1000] + x[30000] + x[60000] + x[90000]
print(x[30000])
print(sx)

# iii)
U = np.zeros(N + 1)
U[0] = 0
U[1] = U[0] + (T / N) * 0.5 
U1 = U[1]
print(U1)

# iv, v)

h = T / N
x = np.linspace(0, T, N + 1)

U = np.zeros(N + 1)
U[0] = 0
U[1] = U[0] + h * 0.5
U1 = U[1]

for n in range(1, N):
    xn = x[n]
    A = (xn**2) / h**2 + xn / h
    B = (2 * xn**2 / h**2 + xn / h) * U[n] - (xn**2 / h**2) * U[n-1] - (xn**2 - 1) * U[n]
    U[n+1] = B / A

# Store results
U1000 = U[1000]
U10000 = U[10000]
U50000 = U[50000]
U100000 = U[100000]

print(f"U1000 = {U1000}")
print(f"U10000 = {U10000}")
print(f"U50000 = {U50000}")
print(f"U100000 = {U100000}")

# vi）
bessel1 = jv(1, x)
normbessel1 = np.linalg.norm(U - bessel1, ord=np.inf)
R5normbessel1 = round(normbessel1, 5)

print(f"normbessel1 = {normbessel1}")
print(f"R5normbessel1 = {R5normbessel1}")