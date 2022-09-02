import random

def generuj():
    yield random.randint(-1000, 1000)
    yield random.randint(-1000, 1000)

liczba = generuj()
print(next(liczba))
print(next(liczba))

#ponizsza linia wygeneruje wyjatek StopIteration
print(next(liczba))