# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'rjftv': 78, 'pceyn': 97, 'ezmii': 93}


def func2():
    return [44, 49, 85]


def func3():
    return (46, 53, 41)


def func4():
    return 93.31


def func5():
    return 'plrei'


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
