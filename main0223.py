# imie = input('Jak masz na imie? ')
imie = 'ttt'
a = 'Cześć {}'.format(imie)
print(a)
print(a[-1])
print(a[2:3])
print(type(a[2:3]))
print(a[2:])
print(a[:3])
print(a[::2])
b = 4
c = 3.2
print("{} {} {}".format(type(a), type(b), type(c)))
lista = ['t1', 't2', 't3', 't4']
print('-'.join(lista).split('-'))
print(lista[2:])
d = 'Metody Inżynierii Wiedzy są najlepsze'
d = d.replace('ą', 'a').replace('ż', 'z')
print('{} {}'.format(d, len(d)))
e = set(d)
print('{} {}'.format(e, len(e)))
f1 = 'string'
f2 = 2
f3 = (f1, f2)
print('{} {}'.format(f3, type(f3)))
lista_c = [1, 5, 8]
lista_l = ['b', 'i', 'a']
print('{}'.format(lista_c + lista_l))
lista_c.append(9)
print(lista_c)
lista_c.insert(0, 2)
print(lista_c)
