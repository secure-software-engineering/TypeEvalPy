# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'zunmi'


def func2():
    return 78


def func3():
    return 23.55


def func4():
    return {'jszvf': 45, 'gvllp': 62, 'bzalq': 91}


def func5():
    return (19, 9, 88)


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
