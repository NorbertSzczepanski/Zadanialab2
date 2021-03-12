import sys as system

print('Zadanie1')
zdanie = input('Napisz zdanie: ')
print(zdanie.count('a'))

print('Zadanie2')
system.stdout.write('Podaj 3 liczby całkowite: ')
a = system.stdin.readline()
b = system.stdin.readline()
c = system.stdin.readline()
a = int(a)
b = int(b)
c = int(c)
system.stdout.write('Wynik (a^b)+c to: ' + str((a ** b) + c))

print('\nZadanie3')
system.stdout.write('Podaj 3 liczby całkowite: ')
d = system.stdin.readline()
e = system.stdin.readline()
f = system.stdin.readline()
d = int(d)
e = int(e)
f = int(f)

if d >= e:
    if d >= f:
        najwiekszaliczba = d
        print('Najwiekszą liczbą jest: ' + str(najwiekszaliczba))
if e >= d:
    if e >= f:
        najwiekszaliczba = e
        print('Największą liczbą jest: ' + str(najwiekszaliczba))
if f >= d:
    if f >= e:
        najwiekszaliczba = f
        print('Największą liczbą jest: ' + str(najwiekszaliczba))
