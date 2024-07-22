# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'gyffo': 81, 'cgbec': 78, 'mvxea': 1}


def func2():
    return [65, 71, 29]


def func3():
    return 'gwqjr'


def func4():
    return 97


def func5():
    return 89.38


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
