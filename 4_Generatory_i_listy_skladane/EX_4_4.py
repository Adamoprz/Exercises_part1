


def fib():
    n = 1

    def fib_gen(n):
        if n == 1:
            return 1
        elif n < 1:
            return 0
        return fib_gen(n-1) + fib_gen(n-2)

    while(1):
        yield fib_gen(n)
        n = n + 1

fib_1 = fib()
print(next(fib_1))
print(next(fib_1))
print(next(fib_1))
print(next(fib_1))
print(next(fib_1))
print(next(fib_1))
print(next(fib_1))
