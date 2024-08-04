# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 11.81


def func2():
    return 'nccfo'


def func3():
    return {'vrblh': 38, 'apjzx': 20, 'jyhaj': 76}


def func4():
    return 4


def func5():
    return (14, 78, 28)


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
