sasiedzi = {
    "Rosja": "Moskwa",
    "Litwa": "Wilno",
    "Białoruś": "Mińsk",
    "Ukraina": "Kijów",
    "Słowacja": "Bratysława",
    "Czechy": "Praga",
    "Niemcy": "Berlin",
}
sasiedzi["Hiszpania"] = "Madryt"
#print(bool(""))
#print(bool(' '))
#print(bool(0))
#print(bool(1))
#print(bool('0'))
#print(bool('1'))
#print(bool([]))
#print(bool([","]))
napis = 'Metody Inżynierii Wiedzy'
#print('i' in napis)
#for i in range(21):
#    print(i)


def split(text, sep):
    a = []
    temp = ''
    for n in text:
        if n == sep:
            a.append(temp)
            temp = ''
        else:
            temp += n
    if temp:
        a.append(temp)
    return a


#print(split(napis, ' '))

def mochasla(haslo):
    if len(haslo) < 10:
        return False
    if '!' not in haslo:
        return False
    mala = False
    duza = False
    for a in haslo:
        if a.islower():
            mala = True
        elif a.isupper():
            duza = True
    return mala and duza


print(mochasla('Haslo!!!!!'))



