class first_class():
    variable1 = 1
    variable2 = 2
    def function(self):
        print('Hello World')

object = first_class()
object.variable1
object2 = first_class()
object2.variable2

print(object.variable1)
print(object2.variable2)

object3 = first_class()
object3.function()
print(object3)

# Możemy wielokrotnie tworzyć obiekty tej samej klasy, gdzie każdy z obiektów będzie naszym niezależnym bytem w
# pamięci programu. A więc wszystkie jego zmienne będą niezależne od instancji tej klasy. Dostęp do funkcji wewnątrz
# obiektu działa tak jak w przypadku dostępu do zmiennej (object3).
#
# Podsumowanie: Klasy w programach obiektowych służą do tworzenia "szablonów",
# w których będą tworzone obiekty, z kolei obiekty będą podstawową jednostką funkcjonalną.

