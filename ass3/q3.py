import numpy as np
from numpy.random import randn, seed

def naiveifft_m(y):
    N = len(y)
    x = np.zeros(N, dtype=complex)

    for n in range(N):
        sum_val = 0
        for k in range(N):
            angle = 2j * np.pi * k * n / N
            sum_val += y[k] * np.exp(angle)
        x[n] = sum_val / N
    return x


results = {}
for m in range(6, 12):
    seed(1)
    ym = randn(2**m)
    xm = naiveifft_m(ym)
    modx20m = abs(xm[20])
    results[f"modx20{m}"] = modx20m

for k, v in results.items():
    print(f"{k} = {v:.8f}")