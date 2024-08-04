# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qecwr': 27, 'vlsgw': 28, 'umitd': 89}


def func2():
    return 20


def func3():
    return 15.02


def func4():
    return (21, 92, 66)


def func5():
    return 'acpge'


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
