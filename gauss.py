import math
import numpy as np

def gauss(a):
    n = len(a[0]) - 1
    x = np.zeros(n)
    for i in range(n):
        if a[i][i] == 0.0:
            pass
        for j in range(n):
            if i != j:
                ratio = a[j][i] / a[i][i]
                for k in range(n + 1):
                    a[j][k] = a[j][k] - ratio * a[i][k]
    for i in range(n):
        x[i] = a[i][n] / a[i][i]
    for i in range(n):
        print(f'X{i} = {x[i]}')

A = np.array([
    [1,1,1,9],
    [2,-3,4,13],
    [3,4,5,40]
], dtype=float)

gauss(A)
