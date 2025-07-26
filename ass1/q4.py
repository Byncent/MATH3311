from math import pi

def compute_pi(n):
    s = 0.0
    for k in range(n):
        s += 1/(16**k) * (4/(8*k+1)-2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6))
    return s

approx = 0
n=0
while approx - pi != 0:
    n += 1
    approx = compute_pi(n)

print(n)