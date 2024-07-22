# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 15


def func2():
    return (73, 27, 31)


def func3():
    return {'cqdzh': 53, 'aucsj': 62, 'dqpct': 94}


def func4():
    return [1, 24, 96]


def func5():
    return 'owzhc'


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
