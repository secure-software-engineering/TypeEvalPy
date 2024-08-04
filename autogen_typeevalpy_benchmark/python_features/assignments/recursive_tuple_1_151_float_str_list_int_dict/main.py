# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 89.15


def func2():
    return 'zdkrr'


def func3():
    return [10, 33, 70]


def func4():
    return 27


def func5():
    return {'mtjxf': 53, 'syuhq': 91, 'ngsnb': 80}


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
