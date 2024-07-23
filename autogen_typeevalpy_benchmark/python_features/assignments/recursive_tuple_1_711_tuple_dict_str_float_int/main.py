# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (20, 17, 56)


def func2():
    return {'lhehh': 61, 'xbqew': 83, 'mybcp': 74}


def func3():
    return 'pykob'


def func4():
    return 82.68


def func5():
    return 52


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
