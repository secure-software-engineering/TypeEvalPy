# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ysrkn': 77, 'rbbmk': 41, 'soolr': 12}


def func2():
    return [87, 84, 28]


def func3():
    return (55, 3, 66)


def func4():
    return 'zvsav'


def func5():
    return 1


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
