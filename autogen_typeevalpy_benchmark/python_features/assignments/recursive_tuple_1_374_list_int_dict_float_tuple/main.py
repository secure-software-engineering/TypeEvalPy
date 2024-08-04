# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [21, 8, 92]


def func2():
    return 58


def func3():
    return {'xstkd': 90, 'dautm': 78, 'qmjbe': 9}


def func4():
    return 77.14


def func5():
    return (34, 3, 51)


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
