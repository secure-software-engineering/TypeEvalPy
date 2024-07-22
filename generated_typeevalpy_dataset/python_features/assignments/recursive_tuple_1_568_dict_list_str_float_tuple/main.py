# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qbgnn': 90, 'iycnh': 17, 'kpolg': 27}


def func2():
    return [63, 23, 8]


def func3():
    return 'pcotx'


def func4():
    return 85.53


def func5():
    return (9, 16, 19)


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
