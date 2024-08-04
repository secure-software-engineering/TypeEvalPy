# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 37


def func2():
    return [74, 58, 82]


def func3():
    return 20.94


def func4():
    return {'wmyjj': 39, 'mkple': 77, 'ymtlc': 69}


def func5():
    return (20, 71, 94)


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
