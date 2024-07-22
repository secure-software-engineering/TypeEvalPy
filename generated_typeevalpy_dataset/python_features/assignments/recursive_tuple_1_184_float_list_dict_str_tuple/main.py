# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 34.51


def func2():
    return [89, 2, 21]


def func3():
    return {'fkhvc': 72, 'vrawd': 66, 'ipqpm': 35}


def func4():
    return 'agtso'


def func5():
    return (81, 25, 22)


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
