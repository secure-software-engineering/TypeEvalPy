# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'pfouu': 91, 'fkusm': 20, 'eadji': 67}


def func2():
    return 100


def func3():
    return 39.69


def func4():
    return 'xaqoq'


def func5():
    return (63, 32, 45)


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
