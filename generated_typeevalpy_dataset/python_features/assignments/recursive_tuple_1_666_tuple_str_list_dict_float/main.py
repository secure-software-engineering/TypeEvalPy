# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (2, 82, 83)


def func2():
    return 'qpdcf'


def func3():
    return [68, 11, 61]


def func4():
    return {'rgsfg': 64, 'yzwsj': 23, 'gxbzc': 56}


def func5():
    return 40.12


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
