# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'mojis'


def func2():
    return 79


def func3():
    return {'hptcw': 73, 'zdjsb': 97, 'gmqrz': 56}


def func4():
    return [88, 25, 42]


def func5():
    return (93, 36, 97)


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
