# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'rtlit': 100, 'grpjg': 25, 'awbir': 81}


def func2():
    return 77.01


def func3():
    return (40, 99, 32)


def func4():
    return [92, 58, 86]


def func5():
    return 3


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
