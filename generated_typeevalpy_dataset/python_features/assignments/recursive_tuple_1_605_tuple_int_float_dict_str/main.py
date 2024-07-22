# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (23, 77, 19)


def func2():
    return 79


def func3():
    return 34.04


def func4():
    return {'pxayt': 2, 'buesb': 64, 'huelh': 27}


def func5():
    return 'tijdk'


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
