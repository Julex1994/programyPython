#Napisz program który wypisze kolejne litery imienia

imie = ['A', 'n', 't', 'e', 'k']

i = 0
while i < len(imie):
    litera = imie[i]
    print(litera)
    i = i + 1

#Napisz program który mając listę [1,2,3,4] pomnoży każdy element listy dwukrotnie

lista1 = [1, 2, 3, 4]

a = 0
while a < len(lista1):
    mnozenie = lista1[a] * 2
    print(mnozenie)
    a = a + 1

#Napisz program który mając listę [1,2,3,4,5,6] wypisze pierwsze trzy element listy, a następnie usunie je z listy
lista2 = [1, 2, 3, 4, 5]
print(lista2[0:3])
del lista2 [0:3]
print(lista2)

#Napisz program który mając listę [1,2,3,4,5,6] wypisze ostatnie trzy element listy, a następnie usunie je z listy
lista3 = [1, 2, 3, 4, 5]
print(lista3[2:])
del lista3 [2:]
print(lista3)