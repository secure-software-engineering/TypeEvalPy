# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [80, 82, 9]


def func2():
    return {'mkzbf': 19, 'spymg': 25, 'nuosa': 49}


def func3():
    return 'rgmlg'


def func4():
    return 39.36


def func5():
    return (97, 92, 100)


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
