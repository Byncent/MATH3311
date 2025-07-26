from numpy import array, pi,sin, linalg
import scipy
import scipy.linalg
m=100
n=100
k=array([range(1,m+1)])
l=array([range(1,n+1)])
A = sin(pi*k.T@l/(m*n))

norm2mat = scipy.linalg.norm(A, 2)

AtA = A.T @ A
eigvals = scipy.linalg.eigvals(AtA)
norm2eig = max(eigvals.real) ** 0.5

print(norm2mat)
print(norm2eig)
print(abs(norm2eig - norm2eig))
print(linalg.cond(A))
