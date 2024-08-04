# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 49


def func2():
    return 'oyjod'


def func3():
    return [11, 38, 57]


def func4():
    return (67, 46, 30)


def func5():
    return {'pmqlm': 66, 'kuije': 70, 'gqjcv': 83}


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
