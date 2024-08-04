# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'vdkjy': 21, 'kjewo': 44, 'cifqp': 42}


def func2():
    return 23.13


def func3():
    return [35, 86, 56]


def func4():
    return 'qalhd'


def func5():
    return 78


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
