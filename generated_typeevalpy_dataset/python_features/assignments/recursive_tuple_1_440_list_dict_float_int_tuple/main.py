# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [78, 93, 24]


def func2():
    return {'wudvb': 34, 'mshre': 9, 'hrdov': 48}


def func3():
    return 76.51


def func4():
    return 25


def func5():
    return (87, 24, 56)


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
