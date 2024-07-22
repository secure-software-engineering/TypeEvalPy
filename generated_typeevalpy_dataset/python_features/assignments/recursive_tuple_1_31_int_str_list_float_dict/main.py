# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 26


def func2():
    return 'nacba'


def func3():
    return [13, 11, 5]


def func4():
    return 57.99


def func5():
    return {'rzxza': 71, 'mglqy': 98, 'pqjfr': 45}


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
