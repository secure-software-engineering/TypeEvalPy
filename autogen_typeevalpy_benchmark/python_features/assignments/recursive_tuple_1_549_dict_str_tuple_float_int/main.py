# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cejdk': 73, 'dtyfr': 82, 'hctsa': 15}


def func2():
    return 'yyyfc'


def func3():
    return (11, 22, 42)


def func4():
    return 55.73


def func5():
    return 14


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
