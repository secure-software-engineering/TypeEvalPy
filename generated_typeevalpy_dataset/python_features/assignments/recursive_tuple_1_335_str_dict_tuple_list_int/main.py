# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'pcxip'


def func2():
    return {'wqrrw': 20, 'lgigr': 75, 'itysv': 48}


def func3():
    return (20, 29, 45)


def func4():
    return [37, 8, 8]


def func5():
    return 43


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
