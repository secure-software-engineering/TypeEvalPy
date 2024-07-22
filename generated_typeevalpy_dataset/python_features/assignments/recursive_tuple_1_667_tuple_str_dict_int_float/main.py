# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (39, 72, 65)


def func2():
    return 'bkuyz'


def func3():
    return {'scckc': 92, 'dbjgx': 61, 'xibbm': 71}


def func4():
    return 89


def func5():
    return 7.99


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
