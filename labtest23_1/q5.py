from numpy import array, zeros, ones, identity, exp, linspace, sin, cos, pi, diag, inf, log
from numpy.linalg import norm, eigvals, cond
from scipy.linalg import lu, solve
from scipy.interpolate import CubicSpline
from scipy.fft import fft

def approx(N):
    h = 1/N
    x = linspace(0,1,N+1)

    d1 = ones(N-1) * (-2 - h ** 2)
    d2 = ones(N-2)
    A = diag(d1) + diag(d2, 1) + diag(d2, -1)

    a = h**2 * (-(pi ** 2 + 1) * sin(pi * x[1:N]) - x[1:N])
    a[-1] -= 1
    return solve(A, a)

U4 = approx(4)

E = zeros(3)
for i in range(3):
    N = 2 ** i * 80
    x = linspace(0,1,N+1)
    u = sin(pi * x[1:N]) + x[1:N]
    U = approx(N)
    E[i] = norm(u - U, inf)
print(E)

from numpy.linalg import solve, norm
from numpy import diag, log, ones, zeros, pi, inf, sin
from numpy import linspace

N=4
x = linspace(0,1,N+1)
U4 = zeros(N-1)
h=1/N
d4=ones(N-2)
d3=ones(N-1)*(-2-h**2)
A=diag(d4,-1)+diag(d3)+diag(d4,1)
a=zeros(N-1)
a[:-1]=-h**2*((pi**2+1)*sin(pi*x[1:-2])+x[1:-2])
a[N-2]=-h**2*((pi**2+1)*sin(pi*x[N-1])+x[N-1])-1

OC = zeros(2)
OC[0] = log(E[0]/E[1])/log(2)
OC[1] = log(E[1]/E[2])/log(2)
print(OC)

U4=solve(A,a)
E=zeros(3)
OC=zeros(2)
for i in range(0,3):
    N=(2**i)*80
    x1 = linspace(0,1,N+1)
    U = zeros(N)
    h1=1/N
    d4=ones(N-2)
    d3=ones(N-1)*(-2-h1**2)
    A1=diag(d4,-1)+diag(d3)+diag(d4,1)

    a1=zeros(N-1)
    a1[:-1]=-h1**2*((pi**2+1)*sin(pi*x1[1:-2])+x1[1:-2])
    a1[N-2]=-h1**2*((pi**2+1)*sin(pi*x1[N-1])+x1[N-1])-1
    U=solve(A1,a1)
    u= (sin(pi*x1[1:N])+x1[1:N]).T
    E[i]=norm(U-u,inf)

OC[0]=log(E[0]/E[1])/log(2)
OC[1]=log(E[1]/E[2])/log(2)

print(OC)