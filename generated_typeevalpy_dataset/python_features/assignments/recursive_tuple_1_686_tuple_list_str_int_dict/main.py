# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (39, 70, 31)


def func2():
    return [18, 95, 65]


def func3():
    return 'ofgnx'


def func4():
    return 4


def func5():
    return {'jznzx': 33, 'nsqag': 81, 'phfff': 30}


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