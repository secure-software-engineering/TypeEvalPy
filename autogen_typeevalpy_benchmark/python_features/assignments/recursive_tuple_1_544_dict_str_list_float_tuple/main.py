# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'dgebg': 9, 'rewxp': 3, 'sjmat': 8}


def func2():
    return 'smpsc'


def func3():
    return [28, 21, 35]


def func4():
    return 37.75


def func5():
    return (100, 31, 71)


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
