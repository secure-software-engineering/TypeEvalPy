# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'oeczz'


def func2():
    return {'zgibn': 11, 'bldcu': 42, 'eeoqh': 28}


def func3():
    return 98


def func4():
    return [89, 37, 17]


def func5():
    return (31, 23, 29)


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
