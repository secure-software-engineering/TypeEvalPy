# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (11, 28, 76)


def func2():
    return {'ipwxa': 15, 'fwdcx': 84, 'gbwva': 5}


def func3():
    return [36, 28, 80]


def func4():
    return 'gnsyp'


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
