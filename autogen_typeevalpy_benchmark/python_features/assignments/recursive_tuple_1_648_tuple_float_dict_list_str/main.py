# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (27, 72, 42)


def func2():
    return 75.73


def func3():
    return {'idjtl': 70, 'gwydf': 68, 'huskr': 68}


def func4():
    return [25, 63, 4]


def func5():
    return 'yhklm'


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
