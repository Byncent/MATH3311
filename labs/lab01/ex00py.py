# MATH3311/MATH5335: File = ex00.py
# Run the file by typing 'run ex00' in an IPython console.
# Soon you will understand the commands used here.
# Try using the mouse to rotate your view of the plot or zoom in

from numpy import linspace, meshgrid, pi, sqrt, exp, cos
import matplotlib.pyplot as plt


xl = [-4, 4] 
nx = 81
yl = [-4, 4] 
ny = 81

x = linspace(xl[0], xl[1], nx)
y = linspace(yl[0], yl[1], ny)

[X, Y] = meshgrid(x, y)

R = X**2 + Y**2
c1 = pi/sqrt(5)
F = exp(-R/2) * cos(c1*R)

fig1 = plt.figure(1)
ax = fig1.add_subplot(projection='3d')
ax.plot_wireframe(X, Y, F)
plt.xlabel('x')
plt.ylabel('y')
plt.title(f'exp( -(x^2+y^2)/2 ) cos( c_1 (x^2+y^2) ), c_1 = {c1}')
plt.show()