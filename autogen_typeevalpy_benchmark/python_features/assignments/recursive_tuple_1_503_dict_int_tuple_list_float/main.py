# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ezwdc': 93, 'fjrov': 40, 'sfdya': 78}


def func2():
    return 83


def func3():
    return (30, 86, 68)


def func4():
    return [78, 6, 69]


def func5():
    return 46.62


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
