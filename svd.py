import numpy as np

A = np.array([
    [1,2,0],
    [2,0,2]
])

# A = np.array([
#     [4,0],
#     [3,-5]
# ])

# LICZENIE U - lewe wektory wlasne
AAT = np.dot(A, A.T)
wartosci_wlasne = np.linalg.eig(AAT)[0]
U = np.linalg.eig(AAT)[1] * -1
kolejnosc = {}
for i in range(wartosci_wlasne.size):
    kolejnosc[i] = i
for i in range(1, wartosci_wlasne.size):
    if wartosci_wlasne[i - 1] < wartosci_wlasne[i]:
        tmp = np.copy(U[:, i - 1])
        U[:, i - 1] = U[:, i]
        U[:, i] = tmp
        tmp = wartosci_wlasne[i - 1]
        wartosci_wlasne[i - 1] = wartosci_wlasne[i]
        wartosci_wlasne[i] = tmp

# LICZENIE E
E = np.zeros((len(A), len(A[0])))
for key, value in kolejnosc.items():
    E[key][key] = np.sqrt(wartosci_wlasne[value])

# LICZENIE V - prawe wektory wlasne
ATA = np.dot(A.T, A)
wartosci_wlasne2 = np.linalg.eig(ATA)[0]

V = np.linalg.eig(ATA)[1]
kolejnosc = {}
for i in range(wartosci_wlasne2.size):
    kolejnosc[i] = i
for i in range(1, wartosci_wlasne2.size):
    if wartosci_wlasne2[i - 1] < wartosci_wlasne2[i]:
        tmp = np.copy(V[:, i - 1])
        V[:, i - 1] = V[:, i]
        V[:, i] = tmp
        tmp = wartosci_wlasne2[i - 1]
        wartosci_wlasne2[i - 1] = wartosci_wlasne2[i]
        wartosci_wlasne2[i] = tmp
V[:, 1:] *= -1

V2 = []
i = 0
while i < len(wartosci_wlasne):
    print(i)
    V2.append(np.dot(A.T, U.T[i]) / np.sqrt(wartosci_wlasne[i]))
    i += 1
while i < len(V):
    V2.append(V.T[i])
    i += 1
V2 = np.array(V2).T

UEVT = np.round(np.dot(np.dot(U, E), V2.T), 2) + 0

print(f'A:\n{A}')
print(f'####')
print(f'U:\n{np.round(U, 2) + 0}')
print(f'E:\n{np.round(E, 2) + 0}')
print(f'VT:\n{np.round(V2.T, 2) + 0}')
print(f'UEVT:\n{UEVT}')

print('#### NUMPY SVD')
U, E_, VT = np.linalg.svd(A)
E = np.zeros((len(A), len(A[0])))
for i in range(len(E_)):
    E[i][i] = E_[i]
UEVT = np.round(np.dot(np.dot(U, E), VT), 2) + 0
print(f'U:\n{np.round(U, 2) + 0}')
print(f'E:\n{np.round(E, 2) + 0}')
print(f'VT:\n{np.round(VT, 2) + 0}')
print(f'UEVT:\n{UEVT}')
