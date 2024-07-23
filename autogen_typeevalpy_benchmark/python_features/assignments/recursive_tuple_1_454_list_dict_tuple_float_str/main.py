# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [35, 90, 78]


def func2():
    return {'pbqty': 53, 'gepzx': 21, 'zszml': 94}


def func3():
    return (33, 4, 49)


def func4():
    return 86.75


def func5():
    return 'bqkgn'


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
