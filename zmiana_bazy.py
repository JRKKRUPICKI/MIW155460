import numpy as np

b = np.array([
    [1,1,1,0,1,0,0,0],
    [1,1,1,0,-1,0,0,0],
    [1,1,-1,0,0,1,0,0],
    [1,1,-1,0,0,-1,0,0],
    [1,-1,0,1,0,0,1,0],
    [1,-1,0,1,0,0,-1,0],
    [1,-1,0,-1,0,0,0,1],
    [1,-1,0,-1,0,0,0,-1],
], dtype=float)

bT = np.array([
    [1,1,1,1,1,1,1,1],
    [1,1,1,1,-1,-1,-1,-1],
    [1,1,-1,-1,0,0,0,0],
    [0,0,0,0,1,1,-1,-1],
    [1,-1,0,0,0,0,0,0],
    [0,0,1,-1,0,0,0,0],
    [0,0,0,0,1,-1,0,0],
    [0,0,0,0,0,0,1,-1]
], dtype=float)

# wektory w macierzy sa ortogonalne (prostopadle)
# macierz diagonalna
diagonalna = np.dot(bT, b)
#print(diagonalna)

# macierz jednostkowa, baza ortonormalna
ortonormalna = diagonalna.copy()
for i in range(len(diagonalna)):
    ortonormalna[i] = diagonalna[i] / np.sqrt(np.dot(diagonalna[i].T, diagonalna[i]))
#print(ortonormalna)

# bT ortonormalna
# macierz jednostkowa
jednostkowa = bT.copy()
for i in range(len(jednostkowa)):
    jednostkowa[i] = jednostkowa[i] / np.sqrt(np.dot(jednostkowa[i].T, jednostkowa[i]))
print(np.round(np.dot(jednostkowa.T, jednostkowa),2)+0)

print(np.dot(jednostkowa, np.array([8,6,2,3,4,6,6,5])))
print(np.dot(jednostkowa.T, np.array([8,6,2,3,4,6,6,5])))
print(np.dot(bT, np.array([8,6,2,3,4,6,6,5])))
print(np.dot(np.linalg.inv(bT), np.array([8,6,2,3,4,6,6,5])))
