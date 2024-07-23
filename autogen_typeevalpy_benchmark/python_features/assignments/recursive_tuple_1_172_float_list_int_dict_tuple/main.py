# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 80.29


def func2():
    return [52, 13, 88]


def func3():
    return 88


def func4():
    return {'ikfbc': 13, 'nyapx': 11, 'ioien': 94}


def func5():
    return (1, 97, 33)


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
