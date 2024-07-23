# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'gymgh'


def func2():
    return 1.68


def func3():
    return 80


def func4():
    return {'avzso': 45, 'wwkvq': 79, 'gpnlk': 77}


def func5():
    return [51, 2, 99]


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
