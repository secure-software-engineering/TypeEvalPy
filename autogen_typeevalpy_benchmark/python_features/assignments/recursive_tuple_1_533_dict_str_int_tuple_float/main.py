# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'htxrs': 67, 'plowv': 95, 'xisjn': 15}


def func2():
    return 'vbdlp'


def func3():
    return 94


def func4():
    return (69, 78, 85)


def func5():
    return 89.82


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
