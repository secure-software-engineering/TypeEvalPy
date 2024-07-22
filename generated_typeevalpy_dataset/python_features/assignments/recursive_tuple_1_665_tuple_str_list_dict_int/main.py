# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (66, 8, 6)


def func2():
    return 'klzic'


def func3():
    return [12, 55, 65]


def func4():
    return {'eyfnx': 70, 'svbkb': 70, 'lqqwc': 36}


def func5():
    return 57


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
