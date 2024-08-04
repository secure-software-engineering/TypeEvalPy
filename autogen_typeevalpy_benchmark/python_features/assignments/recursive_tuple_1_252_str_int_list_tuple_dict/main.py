# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'qhdth'


def func2():
    return 81


def func3():
    return [55, 52, 56]


def func4():
    return (49, 11, 63)


def func5():
    return {'acoph': 70, 'zuusn': 23, 'byhpx': 83}


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
