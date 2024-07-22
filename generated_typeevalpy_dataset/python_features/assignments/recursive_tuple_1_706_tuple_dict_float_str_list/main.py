# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (34, 4, 41)


def func2():
    return {'vdqjx': 43, 'utjiz': 27, 'fcwdl': 2}


def func3():
    return 74.73


def func4():
    return 'ofkgn'


def func5():
    return [88, 16, 24]


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
