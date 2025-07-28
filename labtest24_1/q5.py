
from numpy.linalg import solve, norm
from numpy import diag, exp, ones, zeros, linspace, inf
import numpy as np

def perform_system(N = 5):
    h = 1/N

    x_all = [n*h for n in range(0, N+1)]
    x = x_all[1:-1]

    def p(x):
        return exp(-3*x)

    def q(x):
        return 1

    A = diag([-2] * (N-1)) + diag([1] * (N-2), 1) + diag([1] * (N-2), -1)
    B_init = diag([-1] * (N-2), -1) + diag([1] * (N-2), 1)
    B = diag([p(xi) for xi in x]) @ B_init
    print(f"sumB = {B.sum()}")
    C = diag([q(xi) for xi in x])
    R = np.zeros(N-1)
    R[-1] = 1/h**2 - 3/(2*h) * exp(-3 * (N-1) * h)

    LHS = (-1 / h**2) * A + (3 / (2 * h)) * B + 9*C
    RHS = R
    Uapprox = solve(LHS, RHS)
    return Uapprox

perform_system(5)

def u(x):
    return (1-exp(3*x))/(1-exp(3))

U1 = perform_system(40)
U2 = perform_system(80)

u1_true = np.array([u(x) for x in linspace(0, 1, 41)])[1:-1]
u2_true = np.array([u(x) for x in linspace(0, 1, 81)])[1:-1]

print(U1.shape)
print(u1_true.shape)

print(norm(U1 - u1_true, inf))
print(norm(U2 - u2_true, inf))