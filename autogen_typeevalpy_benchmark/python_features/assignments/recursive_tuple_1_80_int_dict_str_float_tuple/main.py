# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 13


def func2():
    return {'lfnxk': 57, 'xaugm': 85, 'jjxnh': 57}


def func3():
    return 'ejljw'


def func4():
    return 20.65


def func5():
    return (25, 37, 6)


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
