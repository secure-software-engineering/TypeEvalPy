# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [45, 76, 54]


def func2():
    return 68


def func3():
    return (74, 12, 44)


def func4():
    return 'erwqr'


def func5():
    return {'tzzwq': 93, 'vnjqe': 93, 'thpxa': 46}


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
