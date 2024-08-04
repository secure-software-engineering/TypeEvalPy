# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'nmhdg': 82, 'wvhhk': 56, 'tjdcc': 33}


def func2():
    return [78, 95, 97]


def func3():
    return 36.27


def func4():
    return (46, 33, 74)


def func5():
    return 23


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
