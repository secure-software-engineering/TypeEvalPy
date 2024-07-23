# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cmntu': 70, 'gbtvv': 49, 'iubwc': 59}


def func2():
    return (91, 20, 10)


def func3():
    return 53.11


def func4():
    return 'vnxlh'


def func5():
    return [77, 3, 4]


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
