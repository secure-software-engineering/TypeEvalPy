# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'qzayi'


def func2():
    return (89, 99, 71)


def func3():
    return 54


def func4():
    return {'oafch': 80, 'tgupq': 26, 'ryojj': 32}


def func5():
    return [42, 6, 44]


def func6():
    pass


a, (b, c) = func1, (func2, func3)
i = a()
j = b()
k = c()

a, (b, (c, d)) = func1, (func2, (func3, func4))

h = d()

f, b = c, e = func5, func6

l = e()
m = f()
