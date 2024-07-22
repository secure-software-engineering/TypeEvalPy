# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [17, 93, 41]


def func2():
    return {'fidvi': 74, 'tvkhs': 81, 'xrkvk': 74}


def func3():
    return 63


def func4():
    return 8.52


def func5():
    return 'ykqyg'


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
