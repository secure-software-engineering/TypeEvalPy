# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'hweus'


def func2():
    return (48, 44, 70)


def func3():
    return {'rhyxa': 94, 'cjkhh': 14, 'ovnxu': 48}


def func4():
    return 24.9


def func5():
    return 90


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
