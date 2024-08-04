# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fmgky': 80, 'whirn': 55, 'xgcxs': 16}


def func2():
    return (58, 99, 30)


def func3():
    return 3.62


def func4():
    return [74, 76, 21]


def func5():
    return 'rwxid'


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
