# Напишите, свой собственный генератор,
# который отдавал бы N чисел фибоначчи
# (https://ru.wikipedia.org/wiki/Числа_Фибоначчи).
# Дополните функцию fib


def fib(n):
    n1 = 0
    n2 = 1
    while n > 0:
        n -= 1
        v = n1
        n1 = n2
        n2 = n1 + v
        yield v



fib_gen = fib(15)

if __name__ == "__main__":
    print([x for x in fib_gen])
