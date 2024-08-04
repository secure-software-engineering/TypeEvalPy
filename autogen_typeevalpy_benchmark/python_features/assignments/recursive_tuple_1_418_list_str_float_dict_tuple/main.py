# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [79, 58, 2]


def func2():
    return 'bvgww'


def func3():
    return 95.62


def func4():
    return {'dfblx': 70, 'vckvr': 11, 'rqrgw': 31}


def func5():
    return (48, 88, 90)


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
