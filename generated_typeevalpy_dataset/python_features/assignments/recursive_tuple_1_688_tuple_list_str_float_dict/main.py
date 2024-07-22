# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (79, 55, 29)


def func2():
    return [3, 39, 49]


def func3():
    return 'pykql'


def func4():
    return 31.86


def func5():
    return {'dbmng': 44, 'khftb': 67, 'cbqzk': 57}


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
