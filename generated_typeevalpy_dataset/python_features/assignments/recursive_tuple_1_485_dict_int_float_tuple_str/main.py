# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'lopbc': 35, 'vsjds': 1, 'kgbkx': 45}


def func2():
    return 65


def func3():
    return 27.46


def func4():
    return (24, 90, 86)


def func5():
    return 'gqekd'


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
