# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (100, 21, 85)


def func2():
    return 81


def func3():
    return 57.47


def func4():
    return [58, 17, 98]


def func5():
    return {'mifdf': 82, 'eazao': 46, 'cmqma': 68}


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
