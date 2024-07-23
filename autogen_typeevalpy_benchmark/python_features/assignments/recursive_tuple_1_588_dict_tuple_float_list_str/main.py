# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'yzwvw': 80, 'atmry': 33, 'ajjmo': 25}


def func2():
    return (38, 30, 11)


def func3():
    return 37.42


def func4():
    return [10, 96, 87]


def func5():
    return 'tcapv'


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
