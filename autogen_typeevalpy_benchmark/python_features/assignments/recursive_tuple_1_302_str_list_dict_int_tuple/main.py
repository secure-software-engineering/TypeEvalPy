# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'gnmbp'


def func2():
    return [54, 9, 72]


def func3():
    return {'cxdqj': 50, 'kmuxh': 97, 'niiyn': 89}


def func4():
    return 76


def func5():
    return (89, 72, 88)


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
