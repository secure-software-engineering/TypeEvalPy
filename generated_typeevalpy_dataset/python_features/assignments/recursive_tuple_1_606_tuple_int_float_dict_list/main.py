# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (8, 98, 18)


def func2():
    return 15


def func3():
    return 19.16


def func4():
    return {'wkztd': 67, 'ldnpx': 92, 'kvomv': 68}


def func5():
    return [69, 49, 15]


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
