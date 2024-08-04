# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jgqnq': 10, 'frbci': 39, 'znuxh': 65}


def func2():
    return [42, 91, 59]


def func3():
    return (86, 24, 50)


def func4():
    return 'boiuk'


def func5():
    return 68


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
