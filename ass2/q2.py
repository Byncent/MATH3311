import numpy as np
import matplotlib.pyplot as plt

x, y = np.loadtxt('LSdata.dat', unpack=True)

A = np.vstack([x**i for i in range(5)]).T

AT = A.T
ATA = AT @ A
ATy = AT @ y
z = np.linalg.solve(ATA, ATy)

ysol = A @ z

plt.plot(x, y, 'o', label='Data y')
plt.plot(x, ysol, '-', label='Polynomial fit ysol')
plt.xlabel('x')
plt.ylabel('y / ysol')
plt.title('Least Squares Fit: Degree 4 Polynomial')
plt.legend()
plt.show()

err = np.linalg.norm(y - ysol)

sx = np.sum(x)
sy = np.sum(y)
sysol = np.sum(ysol)

print("z = ", z)
print("err = ", err)
print("sx = ", sx)
print("sy = ", sy)
print("sysol = ", sysol)