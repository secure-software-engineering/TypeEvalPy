# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 13.54


def func2():
    return [67, 76, 83]


def func3():
    return {'tiuph': 22, 'uwrme': 61, 'uzcud': 1}


def func4():
    return 42


def func5():
    return 'czdul'


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
