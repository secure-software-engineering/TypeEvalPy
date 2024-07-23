# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'eaofh': 15, 'cgmic': 54, 'phqrc': 62}


def func2():
    return 65


def func3():
    return 'ctxtn'


def func4():
    return [96, 21, 96]


def func5():
    return 28.35


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
