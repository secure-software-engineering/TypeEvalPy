# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 87.06


def func2():
    return [64, 51, 23]


def func3():
    return 'rvkgr'


def func4():
    return {'yiyay': 37, 'pemah': 30, 'wlxoe': 88}


def func5():
    return (55, 37, 66)


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
