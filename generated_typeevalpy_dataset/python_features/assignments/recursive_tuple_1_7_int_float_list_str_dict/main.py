# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 65


def func2():
    return 75.23


def func3():
    return [81, 8, 98]


def func4():
    return 'crmmc'


def func5():
    return {'jziky': 45, 'ghrwc': 78, 'pbctn': 34}


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
