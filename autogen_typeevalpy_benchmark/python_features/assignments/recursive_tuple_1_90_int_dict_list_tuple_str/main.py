# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 23


def func2():
    return {'emsqa': 68, 'eekpb': 18, 'bgxzc': 94}


def func3():
    return [97, 2, 78]


def func4():
    return (13, 49, 50)


def func5():
    return 'avtqb'


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
