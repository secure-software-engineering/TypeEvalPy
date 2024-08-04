# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'xfrya'


def func2():
    return 31


def func3():
    return {'rxiek': 81, 'fxkep': 40, 'qgxrs': 27}


def func4():
    return 94.09


def func5():
    return (84, 95, 35)


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
