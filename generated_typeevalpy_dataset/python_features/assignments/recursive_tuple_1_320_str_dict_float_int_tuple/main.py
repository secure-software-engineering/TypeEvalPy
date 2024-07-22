# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'dxfjc'


def func2():
    return {'iqhat': 16, 'mkdmp': 66, 'jfjvg': 79}


def func3():
    return 34.82


def func4():
    return 71


def func5():
    return (11, 54, 25)


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
