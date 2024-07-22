# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 37.36


def func2():
    return 'qjbac'


def func3():
    return {'hmrgc': 81, 'qpipd': 98, 'yedrw': 29}


def func4():
    return (88, 45, 29)


def func5():
    return 94


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
