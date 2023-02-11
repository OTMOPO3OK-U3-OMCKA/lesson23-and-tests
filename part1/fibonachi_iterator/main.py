# Напишите, свой собственный итератор,
# который отдавал бы N чисел фибоначчи
# (https://ru.wikipedia.org/wiki/Числа_Фибоначчи).
# Для решения задачи нужно дополнить класс Fib
# Достаточно будет сделать итератор только для положительных чисел


class Fib:
    def __init__(self, n):
        self.n = n
        self.n1 = 0
        self.n2 = 1
        self.i = 0

    def __iter__(self):
        return self


    def __next__(self):
        if self.i < self.n:
            self.i += 1
            v = self.n1
            self.n1 = self.n2
            self.n2 = self.n1 + v
            return v
        else:
            raise StopIteration


fib = Fib(15)

if __name__ == "__main__":
    print([x for x in fib])
