# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (58, 40, 47)


def func2():
    return 15


def func3():
    return 'epuui'


def func4():
    return {'qyxzj': 54, 'jktdl': 65, 'cjsgb': 67}


def func5():
    return [49, 47, 94]


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
