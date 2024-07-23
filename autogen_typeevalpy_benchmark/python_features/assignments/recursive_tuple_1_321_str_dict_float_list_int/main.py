# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'yloip'


def func2():
    return {'bhvjm': 47, 'fhrnv': 53, 'bfdfd': 51}


def func3():
    return 31.79


def func4():
    return [30, 28, 34]


def func5():
    return 54


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
