# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'yeqnt'


def func2():
    return (65, 29, 70)


def func3():
    return [16, 21, 30]


def func4():
    return {'womgk': 37, 'jzlsw': 7, 'ucinx': 59}


def func5():
    return 13


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
