# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 19.23


def func2():
    return 'mnhbz'


def func3():
    return (100, 33, 38)


def func4():
    return {'xznbm': 2, 'eroal': 34, 'gdqrl': 94}


def func5():
    return [22, 92, 18]


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
