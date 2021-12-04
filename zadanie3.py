def dodaj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def pomnoz(x, y):
    return x * y

def podziel(x, y):
    return x / y

operacja = input('Podaj działanie: + - * /: ')

liczbaA = int(input('Podaj liczbę: '))
liczbaB = int(input('Podaj liczbę: '))

def wykonaj_dzialanie(operacja):

    if operacja == '*':
        return pomnoz(liczbaA, liczbaB)

    if operacja == '/':
        return podziel(liczbaA, liczbaB)

    if operacja == '+':
        return dodaj(liczbaA, liczbaB)

    if operacja == '-':
        return odejmij(liczbaA, liczbaB)

wynikdzialania = wykonaj_dzialanie(operacja)
print(wynikdzialania)
