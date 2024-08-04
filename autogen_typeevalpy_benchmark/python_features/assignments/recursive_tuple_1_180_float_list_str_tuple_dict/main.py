# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 54.24


def func2():
    return [43, 13, 8]


def func3():
    return 'qpbqw'


def func4():
    return (45, 81, 2)


def func5():
    return {'yhvwp': 34, 'hqkgo': 73, 'rcdsh': 14}


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
