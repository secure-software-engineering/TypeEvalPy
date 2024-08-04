# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 35.83


def func2():
    return (69, 95, 30)


def func3():
    return {'ihxck': 22, 'qqtfw': 42, 'milje': 3}


def func4():
    return [15, 25, 75]


def func5():
    return 'inqho'


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
