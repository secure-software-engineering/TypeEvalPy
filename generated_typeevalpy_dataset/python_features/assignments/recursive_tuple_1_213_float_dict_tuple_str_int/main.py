# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 79.38


def func2():
    return {'irlhe': 57, 'ldefo': 97, 'cpoub': 70}


def func3():
    return (79, 67, 66)


def func4():
    return 'buexs'


def func5():
    return 8


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
