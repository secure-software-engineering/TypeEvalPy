# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'lcbga'


def func2():
    return (7, 45, 44)


def func3():
    return {'ulpyk': 68, 'lsyqh': 48, 'nyutm': 94}


def func4():
    return 77.07


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
