# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (59, 81, 39)


def func2():
    return {'ixyby': 5, 'flwjj': 82, 'weboz': 64}


def func3():
    return 39


def func4():
    return 'pczdp'


def func5():
    return 29.34


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
