# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'gdqzt'


def func2():
    return (44, 70, 49)


def func3():
    return [15, 10, 53]


def func4():
    return 76


def func5():
    return {'qqcsp': 55, 'oqqob': 11, 'upsrm': 27}


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
