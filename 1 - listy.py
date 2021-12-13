#wyciąganie elementów z listy
    #z listy zawierającej liczby
lista1 = [1, 2, 3, 4, 5]
numer_jeden = lista1[0]
print(numer_jeden)

numer_345 = lista1[2:]
print(numer_345)

numer_123 = lista1[:2]
print(numer_123)

numer_ostatni = lista1[-1]
print(numer_ostatni)

    #z listy zawierajacej litery
lista2 = ['K', 'o', 't', 'e', 'k']
litera_t = lista2[2]
print(litera_t)

litera_otek = lista2[1:]
print(litera_otek)

litera_K = lista2[-5]
print(litera_K)

#sprawdzanie długości listy

len(lista1)
len(lista2)
print(len(lista1), len(lista2))

#dołączenie elementu na końcu listy
a = [1, 2, 3]
b = [4, 5]
a.append(b)
print(a)

c = ['O', 'w', 'o']
d = ['c', 'e']
c.append(d)
print(c)

aa = [1, 2, 3]
bb = [4, 5]
aa.extend(bb)
print(aa)

cc = ['O', 'w', 'o']
dd = ['c', 'e']
cc.extend(dd)
print(cc)

#usuwanie wszystkich elementów listy
a.clear()
print(a)

#kopiowanie listy
a1 = [10, 20, 30, 40, 50]
a2 = a1.copy()
print(a2)

#zwracanie ilości elementu na liście
b1 = [1,2,3,1,2,3,1,2,3]
b2 = b1.count(1)
print(b2)

b3 = ['a', 'a', 'a', 'a', 'a']
b4 = b3.count('a')
print(b4)

#okreslanie pozycji
lista_poz = [00, 11, 22, 33, 44, 55]
poz = lista_poz.index(22)
print(poz)

lista_poz2 = ['jabłko', 'gruszka', 'banan']
poz2 = lista_poz2.index('banan')
print(poz2)

#wstawianie elementu do listy na konkretną pozycję
lista_wstaw = [10, 20, 30, 40, 50]
ws1 = lista_wstaw.insert(1, 20000)
print(lista_wstaw)

lista_wstaw2 = ['kurtka', 'spodnie', 'buty']
ws2 = lista_wstaw2.insert(2, 'okulary')
print(lista_wstaw2)

#usunięcie ostatniego elementu listy
lista_usun_ost = [5, 6, 7]
us1 = lista_usun_ost.pop()
print(lista_usun_ost)

lista_usun_ost2 = ['mleko', 'masło', 'jajka']
us2 = lista_usun_ost2.pop()
print(lista_usun_ost2)

#usuwanie elementu z listy
lista_usun = [8, 9, 10]
us1 = lista_usun.remove(9)
print(lista_usun)

lista_usun2 = ['a', 'b', 'c']
us2 = lista_usun2.remove('b')
print(lista_usun2)

#usuwanie kilku elementow
lista_kilka = [1, 2, 3, 4, 5]
del lista_kilka[0:3]
print(lista_kilka)

#odwracanie listy
lista_odwroc = [1, 2, 3, 4, 5]
odwr1 = lista_odwroc.reverse()
print(lista_odwroc)

lista_odwroc2 = ['mały', 'średni', 'duży']
odwr2 = lista_odwroc2.reverse()
print(lista_odwroc2)

#sortowanie listy
lista_num = [2, 3, 1, 8, 5]
num = lista_num.sort()
print(lista_num)

lista_alfa = ['małpa', 'kot', 'papuga', 'pies']
alfa = lista_alfa.sort()
print(lista_alfa)

#personalizowane sortowanie

def wiek(w):
  return w['wiek']

lista_dzieci = [
    {'dziecko': 'Asia', 'wiek': 10},
    {'dziecko': 'Basia', 'wiek': 2},
    {'dziecko': 'Kasia', 'wiek': 15},
]
dz = lista_dzieci.sort(reverse=True, key=wiek)
print(lista_dzieci)

def waga(kg):
    return kg['waga']

lista_zakupow = [
    {'zakup':'jabłko', 'waga':10},
    {'zakup':'ziemniaki', 'waga':6},
    {'zakup':'ogórki', 'waga':3},
]
zkp = lista_zakupow.sort(key=waga)
print(lista_zakupow)









