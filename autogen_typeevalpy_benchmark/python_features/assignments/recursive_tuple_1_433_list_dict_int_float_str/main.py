# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [33, 69, 67]


def func2():
    return {'qzaxn': 46, 'cpzmm': 57, 'ofcpw': 2}


def func3():
    return 35


def func4():
    return 45.17


def func5():
    return 'zkgev'


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
