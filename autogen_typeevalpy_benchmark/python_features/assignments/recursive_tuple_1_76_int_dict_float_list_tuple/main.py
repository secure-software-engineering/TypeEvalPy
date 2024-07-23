# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 75


def func2():
    return {'oelaf': 72, 'ystjt': 90, 'akfjl': 85}


def func3():
    return 87.04


def func4():
    return [7, 8, 80]


def func5():
    return (34, 56, 23)


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
