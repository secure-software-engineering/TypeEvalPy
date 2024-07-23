# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 53


def func2():
    return 31.79


def func3():
    return (57, 31, 95)


def func4():
    return [78, 16, 23]


def func5():
    return {'kmzuk': 8, 'osuvj': 66, 'xhroi': 28}


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
