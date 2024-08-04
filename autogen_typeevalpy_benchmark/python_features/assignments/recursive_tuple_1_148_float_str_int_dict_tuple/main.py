# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 49.86


def func2():
    return 'uopvu'


def func3():
    return 45


def func4():
    return {'zyppc': 30, 'oyhba': 3, 'nqlhw': 8}


def func5():
    return (4, 100, 26)


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
