# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (90, 32, 96)


def func2():
    return 'pssiq'


def func3():
    return {'ovitu': 97, 'dtqnw': 94, 'oswtn': 5}


def func4():
    return [33, 69, 19]


def func5():
    return 32


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
