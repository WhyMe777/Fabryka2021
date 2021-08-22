# Cześć Paweł. Poniżej przygotowany kalkulator.
from math import sqrt

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def remainder(x, y):
    return x % y

def power(x, y):
    return x ** y

print('''
Wybierz operację:
 (1) dodawanie
 (2) odejmowanie
 (3) mnożenie
 (4) dzielenie
 (5) reszta z dzielenia
 (6) potęga
''')

while True:
    choice = input('Wybierz operację (1|2|3|4|5|6): ')

    if choice in ('1', '2', '3', '4', '5', '6'):
        x = float(input('Podaj pierwszą liczbę: '))
        y = float(input('Podaj drugą liczbę: '))

# Część dodana

    if choice == '1':
        print(add(x,y))

    elif choice == '2':
        print(subtract(x, y))

    elif choice == '3':
        print(multiply(x, y))

    elif choice == '4':
        print(divide(x, y))

    elif choice == '5':
        print(remainder(x, y))

    elif choice == '6':
        print(power(x, y))

    elif choice != ('1', '2', '3', '4', '5', '6'):
        print('''
Wybrałeś niepoprawny numer działania.
Wybierz ponownie.
        ''')