# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 16


def func2():
    return {'zsjaz': 73, 'jsrbv': 54, 'wajcc': 20}


def func3():
    return (98, 24, 61)


def func4():
    return [96, 18, 96]


def func5():
    return 'nymsl'


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
