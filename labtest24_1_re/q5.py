from numpy.linalg import solve, norm
from numpy import diag, exp, ones, zeros, linspace, inf

N = 5
h = 1/5
x = linspace(0, 1, N+1)

A = diag(ones(N-2), 1) - 2 * diag(ones(N-1)) + diag(ones(N-2), -1) 
B = diag(exp(-3 * x[1:-1])) @ (diag(ones(N-2), 1) - diag(ones(N-2), -1))
C = diag(ones(N-1))
print(f"A = {A}")
print(f"sumB = {B.sum()}")
print(f"C = {C}")

R = zeros(N-1)
R[-1] = 1/h**2 - 3/(2 * h) * exp(-3 * (N-1) * h)

Uapprox = solve(-1/h**2 * A + 3/(2*h) * B + 9 * C, R)
print(f"Uapprox = {Uapprox}")

def do(N):
    h = 1/N
    x = linspace(0, 1, N+1)

    A = diag(ones(N-2), 1) - 2 * diag(ones(N-1)) + diag(ones(N-2), -1) 
    B = diag(exp(-3 * x[1:-1])) @ (diag(ones(N-2), 1) - diag(ones(N-2), -1))
    C = diag(ones(N-1))
    R = zeros(N-1)
    R[-1] = 1/h**2 - 3/(2 * h) * exp(-3 * (N-1) * h)

    Uapprox = solve(-1/h**2 * A + 3/(2*h) * B + 9 * C, R)


    tsol = (1 - exp(3 * x[1:-1]))/(1-exp(3))
    return norm(tsol - Uapprox, inf)

E = zeros(2)
for i in range(1, 3):
    N = i * 40
    E[i-1] = do(N)

print(E)