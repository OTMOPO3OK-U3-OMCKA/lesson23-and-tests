# Вам дана обычная функция foo, перепишите ее на лямбду функцию.
foo = lambda x: (y**2 for y in range(x))


if __name__ == "__main__":
    print([x for x in foo(5)])
