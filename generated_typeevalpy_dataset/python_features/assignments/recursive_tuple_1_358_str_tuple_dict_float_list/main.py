# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'tjmdw'


def func2():
    return (89, 32, 50)


def func3():
    return {'dzywb': 20, 'ibksb': 55, 'dfmrn': 27}


def func4():
    return 63.23


def func5():
    return [46, 59, 77]


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
