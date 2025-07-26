from numpy import array, zeros, ones, identity, diag, linspace, sqrt
from numpy.linalg import norm, eigvals, cond, lstsq
from matplotlib.pyplot import plot, show
from scipy.linalg import lu, qr
from scipy.interpolate import CubicSpline

tdat = linspace(1, 10, 10)
ydat = array([275.99, 407.67, 509.42, 803.62, 1135, 1652.7, 1221.6, 1068.3, 1265.7, 1480])

teval = linspace(1.5, 9.5, 9)
pp = CubicSpline(tdat, ydat)
yspteval = pp(teval)

A = ones((10, 4))
A[:, 1] = sqrt(tdat)
A[:, 2] = tdat
A[:, 3] = tdat**2

xls = lstsq(A, ydat)[0]
yteval = xls[0] + xls[1] * sqrt(teval) + xls[2] * teval + xls[3] * teval**2

tplt = linspace(1, 10, 91)

ypltspline = pp(tplt)
ypltls = xls[0] + xls[1] * sqrt(tplt) + xls[2] * tplt + xls[3] * tplt**2
plot(tdat,ydat,'*', tplt,ypltspline,tplt,ypltls)
show()