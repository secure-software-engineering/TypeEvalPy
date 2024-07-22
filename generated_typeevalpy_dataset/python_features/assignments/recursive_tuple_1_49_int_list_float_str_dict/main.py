# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 48


def func2():
    return [44, 38, 95]


def func3():
    return 8.16


def func4():
    return 'tkxou'


def func5():
    return {'fdzkx': 92, 'letrg': 65, 'onacy': 13}


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
