# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ncvmz'


def func2():
    return [36, 31, 25]


def func3():
    return 17


def func4():
    return {'helnk': 86, 'irqqq': 30, 'xikcd': 76}


def func5():
    return (16, 61, 90)


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
