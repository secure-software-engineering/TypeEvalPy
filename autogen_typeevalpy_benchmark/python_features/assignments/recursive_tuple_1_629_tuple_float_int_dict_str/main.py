# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (6, 31, 66)


def func2():
    return 37.8


def func3():
    return 70


def func4():
    return {'orhzt': 77, 'rnake': 27, 'scxhl': 27}


def func5():
    return 'sikfy'


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
