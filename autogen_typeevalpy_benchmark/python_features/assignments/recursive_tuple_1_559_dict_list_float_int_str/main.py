# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'rxcam': 96, 'eblac': 23, 'onlas': 26}


def func2():
    return [17, 73, 95]


def func3():
    return 99.03


def func4():
    return 81


def func5():
    return 'ljdrg'


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
