# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'iqtwo'


def func2():
    return [27, 89, 51]


def func3():
    return 11


def func4():
    return {'vwzon': 48, 'ogoyt': 71, 'rumiv': 51}


def func5():
    return 52.79


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
