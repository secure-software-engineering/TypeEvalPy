# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 88


def func2():
    return {'wbaff': 41, 'negeg': 19, 'fsryf': 69}


def func3():
    return 53.95


def func4():
    return 'matii'


def func5():
    return [82, 53, 40]


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
