# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'hmeta'


def func2():
    return 57


def func3():
    return [88, 93, 23]


def func4():
    return {'zdrui': 30, 'vndxw': 30, 'gcjbk': 90}


def func5():
    return 76.95


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
