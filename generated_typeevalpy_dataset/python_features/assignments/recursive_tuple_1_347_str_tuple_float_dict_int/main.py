# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'psvxr'


def func2():
    return (32, 3, 62)


def func3():
    return 34.45


def func4():
    return {'prmhh': 64, 'zhwql': 79, 'timtb': 48}


def func5():
    return 11


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
