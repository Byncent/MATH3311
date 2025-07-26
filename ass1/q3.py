import math
import sys

n = 1
while math.factorial(n) <= sys.maxsize:
    n += 1

print(n-1)