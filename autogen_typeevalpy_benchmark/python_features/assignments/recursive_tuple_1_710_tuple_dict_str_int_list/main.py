# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (11, 94, 69)


def func2():
    return {'jodhs': 4, 'aztsi': 50, 'cnupl': 47}


def func3():
    return 'gheuk'


def func4():
    return 47


def func5():
    return [11, 53, 40]


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
