# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [36, 95, 23]


def func2():
    return (56, 65, 59)


def func3():
    return {'gvqrb': 29, 'mqeqv': 57, 'anuwv': 60}


def func4():
    return 'lpkie'


def func5():
    return 47.34


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
