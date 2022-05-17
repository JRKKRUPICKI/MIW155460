import numpy as np

def f(x):
    return x

def montecarlo(f, a, b, n):
    x = np.random.uniform(a, b, n)
    y = [f(val) for val in x]
    y_mean = np.sum(y) / n
    return (b - a) * y_mean

def rectangle(a, b, f, n):
    dx = (b - a) / n
    result = 0
    for x in range(n):
        x = x * dx + a
        result += f(x) * dx
    return result

print(f'monte: {montecarlo(f,0,1,1000)}')
print(f'rect: {rectangle(0,1,f,1000)}')
