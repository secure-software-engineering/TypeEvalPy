# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'lkcer': 96, 'hcmvt': 73, 'jllpc': 68}


def func2():
    return 53


def func3():
    return 'fnqxv'


def func4():
    return (69, 26, 12)


def func5():
    return 74.89


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
