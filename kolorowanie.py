import math
import numpy as np
import random

def wypisz(a):
    for b in a:
        print(b)

def przydziel_losowe_klasy_decyzyjne(a):
    for b in a:
        b[-1] = random.randint(0, 1)

def podziel_na_klasy_decyzyjne(a):
    wynik = {}
    for b in a:
        if not wynik.__contains__(b[-1]):
            wynik[b[-1]] = []
        wynik[b[-1]].append(b)
    return wynik

def metrykaEuklidesowaWektor(a, b, czyOstatniOdciac=False):
    if czyOstatniOdciac:
        a = a[:-1]
        b = b[:-1]
    c = np.array(a) - np.array(b)
    return math.sqrt(np.dot(c, c))

def znajdz_najmniejsza_odleglosc_w_grupach(zbior):
    wynik_odleglosci = {}
    wynik_wiersze = {}
    for grupa in zbior:
        wynik_odleglosci[grupa] = -1
        wynik_wiersze[grupa] = -1
        for wiersz in zbior[grupa]:
            suma = 0
            for wiersz2 in zbior[grupa]:
                suma += metrykaEuklidesowaWektor(wiersz, wiersz2, True)
            if wynik_odleglosci[grupa] == -1 or suma < wynik_odleglosci[grupa]:
                wynik_odleglosci[grupa] = suma
                wynik_wiersze[grupa] = wiersz
    return wynik_wiersze

def przydziel_nowe_klasy_decyzyjne(klasy, dane):
    liczba_zmian = 0
    for wiersz in dane:
        min_odleglos = -1
        nowa_klasa = -1
        for grupa in klasy:
            if min_odleglos == -1 or metrykaEuklidesowaWektor(wiersz, klasy[grupa], True) < min_odleglos:
                min_odleglos = metrykaEuklidesowaWektor(wiersz, klasy[grupa], True)
                nowa_klasa = grupa
        if wiersz[-1] != nowa_klasa:
            wiersz[-1] = nowa_klasa
            liczba_zmian += 1
    return liczba_zmian

file = open('australian.dat', 'r')
data = []
for line in file:
    wynik = list(map(lambda word: float(word), line.replace('\n', '').split(' ')))
    data.append(wynik)

przydziel_losowe_klasy_decyzyjne(data)
podzial = podziel_na_klasy_decyzyjne(data)
najmniejsze = znajdz_najmniejsza_odleglosc_w_grupach(podzial)
zmian = przydziel_nowe_klasy_decyzyjne(najmniejsze, data)
while zmian > 0:
    print(zmian)
    podzial = podziel_na_klasy_decyzyjne(data)
    najmniejsze = znajdz_najmniejsza_odleglosc_w_grupach(podzial)
    zmian = przydziel_nowe_klasy_decyzyjne(najmniejsze, data)
wypisz(data)
