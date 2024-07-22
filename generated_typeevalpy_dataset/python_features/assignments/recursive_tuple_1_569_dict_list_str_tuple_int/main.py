# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'myhcq': 51, 'jtbzt': 1, 'wtgbc': 23}


def func2():
    return [41, 17, 85]


def func3():
    return 'xsbxl'


def func4():
    return (78, 96, 93)


def func5():
    return 61


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
