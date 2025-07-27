from numpy.linalg import solve, norm
from numpy import diag, exp, ones, zeros, linspace, inf, array
import numpy as np



def approx(N):
    h = 1/N
    x = linspace(0, 1, N+1)

    A = diag(-ones(N-1) * 2) + diag(ones(N-2), 1) + diag(ones(N-2), -1)

    B = diag(exp(-3 * x[1 : -2]) * ones(N-2), 1) - diag(exp(-3 * x[2 : -1]) * ones(N-2), -1)
    C = diag(ones(N-1))
    R = zeros(N-1)
    R[-1] =  1/h**2 - 3/(2*h) * exp(-3 * (N-1) * h)
    Uapprox = solve((-1/h**2) * A + 3 / (2 * h) * B + 9 * C, R)
    return Uapprox

U1 = approx(40)
U2 = approx(80)

x1 = linspace(0, 1, 41)[1 : -1]
x2 = linspace(0, 1, 81)[1 : -1]

u1 = (1-exp(3*x1))/(1-exp(3))
u2 = (1-exp(3*x2))/(1-exp(3))

E = zeros(2)
E[0] = norm(U1 - u1, inf)
E[1] = norm(U2 - u2, inf)
print(E)

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