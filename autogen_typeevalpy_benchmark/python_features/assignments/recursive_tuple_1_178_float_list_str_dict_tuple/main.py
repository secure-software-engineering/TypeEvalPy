# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 17.9


def func2():
    return [68, 63, 18]


def func3():
    return 'tokhl'


def func4():
    return {'hxrnp': 43, 'jqdnf': 96, 'psngm': 93}


def func5():
    return (18, 22, 68)


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
