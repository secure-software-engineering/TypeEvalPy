# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ejieo': 80, 'xslnx': 49, 'urcql': 72}


def func2():
    return 91.13


def func3():
    return [29, 47, 95]


def func4():
    return 97


def func5():
    return (61, 49, 1)


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
