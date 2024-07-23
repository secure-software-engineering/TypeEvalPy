# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'uylsc': 7, 'zcutq': 67, 'cxeho': 94}


def func2():
    return (31, 69, 63)


def func3():
    return 6


def func4():
    return [72, 37, 5]


def func5():
    return 69.34


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
