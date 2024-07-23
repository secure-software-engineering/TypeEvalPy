# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'tmrph': 52, 'tsvzq': 43, 'wmfjo': 59}


def func2():
    return 30


def func3():
    return (19, 96, 73)


def func4():
    return [19, 1, 43]


def func5():
    return 'neggp'


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
