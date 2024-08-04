# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ucylu': 29, 'xryhf': 15, 'evexj': 57}


def func2():
    return (21, 73, 36)


def func3():
    return 57


def func4():
    return [56, 31, 72]


def func5():
    return 1.53


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
