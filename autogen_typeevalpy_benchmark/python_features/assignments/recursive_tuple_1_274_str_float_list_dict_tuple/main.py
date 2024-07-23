# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jvyzp'


def func2():
    return 7.52


def func3():
    return [94, 76, 85]


def func4():
    return {'dzpsh': 88, 'fjbqk': 82, 'ijgnp': 91}


def func5():
    return (73, 70, 39)


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
