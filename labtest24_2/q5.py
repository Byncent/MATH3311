from numpy.linalg import solve, norm
from numpy import diag, exp, ones, zeros, linspace, inf

N = 5
h = 1/N
x = linspace(0, 1, N+1)
A = diag(ones(N-2), 1)  - diag(2 * ones(N-1)) + diag(ones(N-2), -1)
B = diag(exp(x[1:-1] - 1)) @ (diag(ones(N-2), 1) - diag(ones(N-2), -1))
C = diag(ones(N-1))
R = zeros(N-1)
R[0] = 1/h**2 - 1/(2 * h) * exp(h - 1)
print(f"A = {A}")
print(f"sumB = {B.sum()}")
print(f"C = {C}")
print(f"R = {R}")

Uapprox = solve(-1/h**2 * A - 1/(2 * h) * B + C, R)
print(f"Uapprox = {Uapprox}")

def approx(N = 5):
    h = 1/N
    x = linspace(0, 1, N+1)
    A = diag(ones(N-2), 1)  - diag(2 * ones(N-1)) + diag(ones(N-2), -1)
    B = diag(exp(x[1:-1] - 1)) @ (diag(ones(N-2), 1) - diag(ones(N-2), -1))
    C = diag(ones(N-1))
    R = zeros(N-1)
    R[0] = 1/h**2 - 1/(2 * h) * exp(h - 1)

    Uapprox = solve(-1/h**2 * A - 1/(2 * h) * B + C, R)
    tol = (1-exp(1-x[1:-1]))/(1-exp(1))
    print(norm(Uapprox - tol, inf))

approx(40)
approx(80)

    


