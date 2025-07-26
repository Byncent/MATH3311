from math import log
m = 10**3
n = 10**2
p = 10**(-2)
q = 1-p

sol = 0
for i in range(1, m+n+1):
    sol += log(i)

for i in range(1, m+1):
    sol -= log(i)

for i in range(1, n+1):
    sol -= log(i)

sol += m * log(p) + n * log(q)
print(sol)