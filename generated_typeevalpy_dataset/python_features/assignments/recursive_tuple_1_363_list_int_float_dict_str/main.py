# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [81, 9, 54]


def func2():
    return 81


def func3():
    return 65.23


def func4():
    return {'vizgw': 60, 'cucub': 32, 'qqzsh': 14}


def func5():
    return 'qvcii'


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
