# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 67


def func2():
    return 94.42


def func3():
    return [11, 44, 41]


def func4():
    return 'kulka'


def func5():
    return {'xdozz': 36, 'uwzkx': 68, 'swsii': 79}


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
