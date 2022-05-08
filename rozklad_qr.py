import math
import numpy as np

# https://adrianstoll.com/linear-algebra/qr-decomposition.html

def iloczynSkalarny(wektorA, wektorB):
    return np.dot(np.array(wektorA.T), np.array(wektorB))

def projekcja(wzgledemWektora, wektor):
    #print(f'OBLICZANIE PROJEKCJI:')
    licznik = iloczynSkalarny(wektor, wzgledemWektora)
    mianownik = iloczynSkalarny(wzgledemWektora, wzgledemWektora)
    #print(f'L: {licznik}')
    #print(f'M: {mianownik}')
    #print(f'WZGLEDEM:\n{wzgledemWektora}')
    #print(f'RETURN:\n{licznik / mianownik * wzgledemWektora}')
    return licznik / mianownik * wzgledemWektora

def oblicz_e(wektor):
    #print(f'OBLICZANIE e:')
    #print(f'RETURN:\n{np.dot(wektor, 1/math.sqrt(np.dot(wektor.T, wektor)))}\n')
    return np.dot(wektor, 1/math.sqrt(np.dot(wektor.T, wektor)))

def qr(macierz):
    #print(f'################################ OBLICZANIE e1')
    wektor_v = np.array(A[:,0]).reshape((3,1))
    wektor_u = wektor_v
    wektor_e = oblicz_e(wektor_u)
    Q = []
    U = []
    Q.append(wektor_e[:,0])
    U.append(wektor_u)
    #print(f'v1:\n{wektor_v}')
    #print(f'u1:\n{wektor_u}')
    #print(f'e1:\n{wektor_e}')
    for i in range(1, len(macierz[0])):
        #print(f'################################ OBLICZANIE e{i + 1}')
        wektor_v = np.array(A[:,i]).reshape((len(macierz),1))
        suma_projekcji = 0
        for j in range(i):
            suma_projekcji += projekcja(U[j], wektor_v)
        wektor_u = wektor_v - suma_projekcji
        U.append(wektor_u)
        wektor_e = oblicz_e(wektor_u)
        Q.append(wektor_e[:, 0])
        #print(f'v{i + 1}:\n{wektor_v}')
        #print(f'u{i + 1}:\n{wektor_u}')
        #print(f'e{i + 1}:\n{wektor_e}')
    #print(f'################################ WYNIK')
    #print(f'A:\n{macierz}')
    #print(f'Q:\n{np.round(np.array(Q).T,3)+0}')
    R = np.dot(np.array(Q), A)
    #print(f'R:\n{np.round(np.array(R),3)+0}')
    QR = np.dot(np.array(Q).T, R)
    # + 0 usuwa minus przy liczie zero np. -0 -> 0
    #print(f'QR:\n{np.round(np.array(QR),3)+0}')
    return np.round(np.array(Q).T,3)+0, np.round(np.array(R),3)+0

def AkPlus1(A):
    Q = qr(A)[0]
    return np.round(np.dot(np.dot(np.linalg.inv(Q), A), Q),3)+0

def czyMacierzGornaTrojkatna(macierz):
    for i in range(1, len(macierz)):
        for j in range(i):
            if macierz[i][j] != 0:
                return False
    return True

A = np.array([
    [1,0,1],
    [1,1,0],
    [0,1,1]
])
