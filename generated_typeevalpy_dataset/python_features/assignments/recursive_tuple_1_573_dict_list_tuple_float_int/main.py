# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cjjfk': 16, 'rvgec': 82, 'hmfgn': 11}


def func2():
    return [45, 26, 53]


def func3():
    return (55, 30, 84)


def func4():
    return 5.93


def func5():
    return 17


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
