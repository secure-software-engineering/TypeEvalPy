# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 63.5


def func2():
    return (71, 87, 48)


def func3():
    return {'plwxq': 39, 'hzufd': 28, 'zklze': 3}


def func4():
    return 57


def func5():
    return 'csvjv'


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
