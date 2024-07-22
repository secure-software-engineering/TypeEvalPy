# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 96.06


def func2():
    return (35, 66, 34)


def func3():
    return {'fhecj': 34, 'dndto': 84, 'gzrzw': 16}


def func4():
    return 'ictjy'


def func5():
    return [64, 9, 22]


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
