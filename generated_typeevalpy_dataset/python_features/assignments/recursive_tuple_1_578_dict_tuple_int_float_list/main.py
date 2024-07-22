# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'yoxuy': 15, 'epmex': 10, 'xdlfw': 73}


def func2():
    return (9, 14, 48)


def func3():
    return 54


def func4():
    return 81.29


def func5():
    return [33, 98, 30]


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
