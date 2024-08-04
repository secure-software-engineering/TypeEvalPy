# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [93, 85, 22]


def func2():
    return (9, 46, 68)


def func3():
    return 78.78


def func4():
    return 'nxsro'


def func5():
    return {'lunfj': 6, 'ocpit': 91, 'rmsco': 7}


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
