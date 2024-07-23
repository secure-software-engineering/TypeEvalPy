# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 11


def func2():
    return 'qhtwh'


def func3():
    return (25, 38, 82)


def func4():
    return {'roqlk': 27, 'fmcxt': 47, 'tqjfj': 31}


def func5():
    return 50.3


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
