import sys as system

print('Zadanie1')
zdanie = input('Napisz zdanie: ')
ilosca = zdanie.count('a')
print('Litera "a" wystąpiła %d razy w zdaniu.' % ilosca)

print('\nZadanie2')
system.stdout.write('Podaj liczbę całkowitą "a": ')
a = int(system.stdin.readline())
system.stdout.write('Podaj liczbę całkowitą "b": ')
b = int(system.stdin.readline())
system.stdout.write('Podaj liczbę całkowitą "c": ')
c = int(system.stdin.readline())
wzor = a ** b + c
system.stdout.write('Wynik działania (a^b)+c to: %d' % wzor)

print('\n\nZadanie3')
system.stdout.write('Podaj liczbę całkowitą "a": ')
a = int(system.stdin.readline())
system.stdout.write('Podaj liczbę całkowitą "b": ')
b = int(system.stdin.readline())
system.stdout.write('Podaj liczbę całkowitą "c": ')
c = int(system.stdin.readline())

najwiekszaliczba = a
if najwiekszaliczba < b:
    najwiekszaliczba = b
    if najwiekszaliczba < c:
        najwiekszaliczba = c
print('Największa liczba to %d' % najwiekszaliczba)

print('\nZadanie4')
liczby = [4, 5.16, 2, 98, 4.15, 8.9, 12, 54, 100.5, 67.2, 14.4, 82]
print(liczby)

counter = 0
for element in liczby:
    liczby[counter] = liczby[counter] ** 2
    counter += 1
print('Liczby z listy "liczby" podniesione do kwadratu: ' + str(liczby))

print('\nZadanie5')
parzyste = []

counter = 0
while counter != 10:
    liczba = int(input('Podaj liczbę całkowitą: '))
    if liczba % 2 == 0:
        parzyste.append(liczba)
    counter += 1
else:
    print('Liczby parzyste: ' + str(parzyste))
