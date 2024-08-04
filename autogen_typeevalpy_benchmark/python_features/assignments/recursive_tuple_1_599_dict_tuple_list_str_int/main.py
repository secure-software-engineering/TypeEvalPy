# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'itgcs': 63, 'gupva': 83, 'umcrb': 82}


def func2():
    return (53, 95, 13)


def func3():
    return [38, 29, 59]


def func4():
    return 'nxgfb'


def func5():
    return 94


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
