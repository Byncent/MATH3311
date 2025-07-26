import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def f(z):
    return np.exp(z) - 2 * z**2

def df(z):
    return np.exp(z) - 4 * z

# i)
z_vals = np.linspace(0, 2, 21)
fz = f(z_vals)
dfz = df(z_vals)
print(f"fz: {fz}")
print(f"dfz: {dfz}")

# ii)
plt.plot(z_vals, fz, label='f(z)')
plt.axhline(-0.5, color='r', linestyle='--', label='f(z) = -0.5')
plt.xlabel('z')
plt.ylabel('f(z)')
plt.grid(True)
plt.legend()
plt.title('Plot of f(z)')
plt.show()

idx = np.argmin(np.abs(fz + 0.5))
z0 = z_vals[idx]
print(f"Chosen starting point z0 = {z0:.6f}, f(z0) = {fz[idx]:.6f}")

# iii)
zn = [z0]
tolerance = 1e-15
max_iter = 50

for i in range(max_iter):
    z_curr = zn[-1]
    fz_curr = f(z_curr)
    dfz_curr = df(z_curr)

    if abs(fz_curr) < tolerance:
        break

    z_next = z_curr - fz_curr / dfz_curr
    zn.append(z_next)

print(f"zn: {zn}")

print("\nNewton Method Iteration Table")
print("Iter |     Approximation      |     Function value")
print("-----|------------------------|------------------------")
for i in range(1, len(zn)):
    approx = zn[i]
    fval = f(approx)
    print(f"{i:>4} | {approx: .16e} | {fval: .16e}")

# iv)
zm = fsolve(f, z0)[0]
fzm = f(zm)

# v)
diffnm = zn[-1] - zm
print(f"\nResult from fsolve: zm = {zm:.16e}, f(zm) = {fzm:.16e}")
print(f"Difference (zn[-1] - zm) = {diffnm:.1e}")