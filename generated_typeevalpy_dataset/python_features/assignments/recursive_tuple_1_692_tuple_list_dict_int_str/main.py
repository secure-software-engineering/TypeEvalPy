# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (76, 16, 88)


def func2():
    return [14, 39, 9]


def func3():
    return {'godsk': 61, 'fsekc': 33, 'gmiff': 18}


def func4():
    return 64


def func5():
    return 'ozsxb'


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
