# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 99


def func2():
    return [17, 82, 60]


def func3():
    return 'icbxp'


def func4():
    return 26.52


def func5():
    return {'snrkt': 80, 'gpvju': 32, 'xwynr': 93}


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
