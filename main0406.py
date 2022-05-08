import math
import numpy as np


################
# 03.09
################


file = open('australian.dat', 'r')
data = []
for line in file:
    #data.append(line.replace('\n', '').split(' '))
    wynik = list(map(lambda word: float(word), line.replace('\n', '').split(' ')))
    data.append(wynik)

def metrykaEuklidesowa(listaA, listaB):
    wynik = 0
    for i in range(len(listaA) - 1):
        wynik += (listaA[i] - listaB[i]) ** 2
    return math.sqrt(wynik)

def zad1():
    wynik = {}
    for i in range(1, len(data)):
        if not wynik.keys().__contains__(data[i][-1]):
            wynik[data[i][-1]] = []
        wynik[data[i][-1]].append(metrykaEuklidesowa(data[0], data[i]))
    return wynik

macierz = [
    [6,9,6,8,9,6],
    [3,8,9,6,1,1],
    [2,6,4,8,6,8],
    [4,7,3,8,9,5],
    [3,9,6,4,2,3],
    [7,5,9,7,2,4],
]

def wyznacznik(m):
    if len(m) == 1:
        return m[0][0]
    a = 0
    for i in range(len(m)):
        n = [row[:] for row in m][1:]
        for row in n:
            del row[i]
        a += m[0][i] * (-1) ** (1+i+1) * wyznacznik(n)
    return a


################
# 03.16
################


# para (klasaDecyzyjna, [odledlosci])
def def1(x, lista):
    wynik = []
    for linia in lista:
        klasaDecyzyjna = linia[-1]
        odleglosc = metrykaEuklidesowa(x, linia)
        wynik.append((klasaDecyzyjna, odleglosc))
    return wynik

# para () z def1 do slownika {klasaDecyzyjna: [odleglosci]}
def def2(list):
    wynik = {}
    for item in list:
        if not wynik.__contains__(item[0]):
            wynik[item[0]] = []
        wynik[item[0]].append(item[1])
    return wynik

# dir klasa suma najmneijszych odlegloci
def def3(dir, k):
    wynik = {}
    for a in dir:
        dir[a].sort()
        wynik[a] = 0
        for i in range(k):
            wynik[a] += dir[a][i]
    return wynik

def decyzja(list, x):
    decyzjaKlasa = None
    decyzjaWartosc = None
    for key, value in def3(def2(def1(x, list)), 5).items():
        if decyzjaKlasa is None:
            decyzjaKlasa = key
            decyzjaWartosc = value
        if value < decyzjaWartosc:
            decyzjaKlasa = key
            decyzjaWartosc = value
    return decyzjaKlasa

x = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

#print(decyzja(data, x))


################
# 03.23
################


def metrykaEuklidesowaWektor(a, b, czyOstatniOdciac=False):
    if czyOstatniOdciac:
        a = a[:-1]
        b = b[:-1]
    c = np.array(a) - np.array(b)
    return math.sqrt(np.dot(c, c))

#print(metrykaEuklidesowaWektor([1,2,3], [3,4,6], True))
#print(metrykaEuklidesowa([1,2,3], [3,4,6]))

##### kolorowanie - zadanie 1

# 28 luty 1h 10m wyklad

# pierwsze kolorowanie losowe
# punkt ciezkosci
# odleglosc miedzy kropka a pozostalymi (kropka = wektor)
# waga kropki ^^
# waga( kropka, zbior kropek)
# zsumowa i zwrocic jako wynik ^^

# kropka - waga
# znalezc mininum wage ^^
# min( zbior kropek wag ) zwrocic kropke - srodek ciezkosci dla dwoch kolorow
# przekolorowac kropki
# po wszystkich kropkach i sprawdzac do krorego koloru jest blizej i wtedy kolorowanuie

########## zadanie 2

# uogolnienie sumy - calka (powie powierzchni pod funkcja)
# metoda monte carlo
# maksimum funkcji na przedziale (dla kazdego x z przedzialu znalezc najwiekszego y)
# proporcja ile pkt jest nad funkcja, a ile pod
# d1 * d2 * proporcja (np 70/100)

######### zadanie 3

# suma gorna, dolna calki
# zmniejszanie przedzialu az sumy beda rowne
# ciecie przedzialu na rowne czesci
# metoda prostokatow

# test czy dobrze liczy
# y = x dla przedzialy 0 - 1 wartosc to 0,5

def australian2():
    wynik = []
    for d1 in data:
        wartosc = 0
        for d2 in data:
            wartosc += metrykaEuklidesowa(d1, d2)
        wynik += wartosc
    wynik.sort()
    return wynik

#australian2()
# metoda k srednich


################
# 03.30
################


def sredniaWektor(a, rodzaj=0):
    # srednia kolumnowa
    if rodzaj == 1:
        return np.mean(np.array(a), 0)
    # srednia wierszowa
    if rodzaj == 2:
        return np.mean(np.array(a), 1)
    # srednia ze wszystkich elementow
    return np.mean(np.array(a))

#print(sredniaWektor([[3,4,2]]))
#print(sredniaWektor([[3,4,2],[4,2,1]]))

def wariancjaWektor(a, rodzaj=0):
    # kolumna
    if rodzaj == 1:
        return np.var(np.array(a), 0)
    # wiersz
    if rodzaj == 2:
        return np.var(np.array(a), 1)
    # wszystko
    return np.var(np.array(a))

def odchylenieWektor(a, rodzaj=0):
    # kolumna
    if rodzaj == 1:
        return np.std(np.array(a), 0)
    # wiersz
    if rodzaj == 2:
        return np.std(np.array(a), 1)
    # wszystko
    return np.std(np.array(a))

#print(np.sqrt(wariancjaWektor([[3,4,2]],2)))
#print(np.sqrt(wariancjaWektor([[3,4,2],[4,2,1]],2)))
#print(odchylenieWektor([[3,4,2]],2))
#print(odchylenieWektor([[3,4,2],[4,2,1]],2))

def srednia(wektory):
    return np.sum(wektory, 0) / len(wektory)

def wariancja(wektory):
    suma = 0
    sw = srednia(wektory)
    for wektor in wektory:
        suma += (np.array(wektor) - sw) ** 2
    return suma / len(wektory)

def odchylenie(wektory):
    return np.sqrt(wariancja(wektory))

wektory = [
    [1,4,3],
    [6,3,3],
    [8,6,2]
]
#print(srednia(wektory))
#print(np.mean(wektory, 0))
#print(wariancja(wektory))
#print(np.var(wektory, 0))
#print(odchylenie(wektory))
#print(np.std(wektory, 0))


def sredniaW(wektor):
    return np.dot(wektor, np.ones(len(wektor), dtype=int)) / len(wektor)

wektor = [2,3,4]
#print(sredniaW(wektor))

def wariancjaW(wektor):
    sw = sredniaW(wektor)
    suma = 0
    for w in wektor:
        suma += (w - sw) ** 2
    return suma / len(wektor)

#print(wariancjaW(wektor))

################
# 04.06
################

