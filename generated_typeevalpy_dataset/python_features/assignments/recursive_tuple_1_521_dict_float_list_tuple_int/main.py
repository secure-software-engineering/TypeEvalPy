# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'vohkx': 98, 'wncwk': 86, 'thajs': 46}


def func2():
    return 34.96


def func3():
    return [52, 27, 27]


def func4():
    return (58, 23, 4)


def func5():
    return 44


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
