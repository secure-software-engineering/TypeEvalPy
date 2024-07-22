# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 46.37


def func2():
    return [90, 69, 83]


def func3():
    return (17, 59, 49)


def func4():
    return 52


def func5():
    return 'qifyj'


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
