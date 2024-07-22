# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'xflfb': 75, 'ijqvx': 60, 'bwick': 25}


def func2():
    return 62


def func3():
    return 'rwaaa'


def func4():
    return 37.81


def func5():
    return [94, 46, 83]


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
