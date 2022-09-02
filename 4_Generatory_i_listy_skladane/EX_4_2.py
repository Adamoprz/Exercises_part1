
def generuj_l_pierwsz():
    i = 2

    def czy_pierwsza(n):
        l_dz = 0
        for i in range(2, n):
            if n % i == 0:
                l_dz = l_dz + 1
        return l_dz

    for a in range(1, 100):
        if czy_pierwsza(i) == 0:
            yield i
        i += 1

lp = generuj_l_pierwsz()
print(next(lp))
print(next(lp))
print(next(lp))
print(next(lp))
print(next(lp))
print(next(lp))
print(next(lp))