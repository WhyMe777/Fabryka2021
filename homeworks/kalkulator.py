# Cześć Paweł. Poniżej przygotowany kalkulator.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("""
Wybierz operację:
  1.Dodawanie
  2.Odejmowanie
  3.Mnożenie
  4.Dzielenie
""")

while True:
    choice = input("Wybierz operację (1|2|3|4): ")

    if choice in ('1', '2', '3', '4'):
        x = float(input("Podaj pierwszą liczbę: "))
        y = float(input("Podaj drugą liczbę: "))

# Część dodana

    if choice == "1":
        print(add(x,y))
        break
    elif choice == '2':
        print(subtract(x, y))
        break
    elif choice == '3':
        print(multiply(x, y))
        break
    elif choice == "4":
        print(divide(x, y))
        break
    elif choice != ('1', '2', '3', '4'):
        print('''
Wybrałeś niepoprawny numer działania.
Wybierz ponownie.
        ''')

#
# else:
#     print("Błędna wartość, podaj poprawną")