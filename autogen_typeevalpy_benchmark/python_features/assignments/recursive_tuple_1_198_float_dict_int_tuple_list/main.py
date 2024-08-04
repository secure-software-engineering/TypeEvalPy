# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 49.85


def func2():
    return {'xilqx': 13, 'xyvob': 49, 'iapsv': 66}


def func3():
    return 93


def func4():
    return (11, 44, 82)


def func5():
    return [96, 39, 55]


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
