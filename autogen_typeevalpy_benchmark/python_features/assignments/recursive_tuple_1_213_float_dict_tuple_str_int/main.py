# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 56.57


def func2():
    return {'ilzym': 69, 'izmeb': 24, 'lhylq': 25}


def func3():
    return (100, 14, 98)


def func4():
    return 'ghhtm'


def func5():
    return 88


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
