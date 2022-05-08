import numpy as np

# regresja liniowa

# y = ax + b

# XB = y
# X macierz
# 1 x1
# 1 x2
# .
# 1 xn

# B wektor
# b0
# b1

# y wektor
# y1
# y2
# .
# yn

#b0 + x1*b1 = y1
#b0 + x2*b1 = y2
# .
#b0 + b1x1 = yn

# b = y/x

# XB=y
# XTXB = XTy
# (XTX)^-1 * (XTX) * B = XTy
# B = (XTX)^-1 * XTy

# y = ax + b
# XB=y
# b0 to b
# b1 to a

# punkty:
# (2,1)
# (5,2)
# (7,3)
# (8,3)
# B = [ 2/7 5/14 ] a = 5/14, b = 2/7

def znajdzB(punkty):
    x = []
    y = []
    for punkt in punkty:
        x.append([1, punkt[0]])
        y.append(punkt[1])
    x = np.array(x)
    y = np.array(y)
    xt = np.transpose(x)
    xtx = np.dot(xt, x)
    xtx1 = np.linalg.inv(xtx)
    xtx1xt = np.dot(xtx1, xt)
    xtx1xty = np.dot(xtx1xt, y)
    return xtx1xty

punkty = [
    [2,1],
    [5,2],
    [7,3],
    [8,3]
]
B = znajdzB(punkty)
print(f'y = {B[1]} * x + {B[0]}')

import matplotlib.pyplot as plt

x = [2,5,7,8]
y = [1,2,3,3]
plt.scatter(x, y)
xx = np.linspace(0,8,100)
yy = B[1] * xx + B[0]
plt.plot(xx, yy, label=f'y = {round(B[1],2)} * x + {round(B[0],2)}')
plt.legend(loc='upper left')
plt.show()
