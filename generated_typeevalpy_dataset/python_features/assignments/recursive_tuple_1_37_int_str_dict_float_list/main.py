# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 9


def func2():
    return 'lmtmq'


def func3():
    return {'xsgfo': 32, 'jqtxc': 20, 'gpjka': 6}


def func4():
    return 43.81


def func5():
    return [22, 31, 19]


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
