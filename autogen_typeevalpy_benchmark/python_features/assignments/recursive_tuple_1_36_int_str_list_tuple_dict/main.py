# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 67


def func2():
    return 'vvsyk'


def func3():
    return [68, 85, 5]


def func4():
    return (25, 13, 52)


def func5():
    return {'xvrfo': 59, 'gyeim': 5, 'habfj': 77}


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
