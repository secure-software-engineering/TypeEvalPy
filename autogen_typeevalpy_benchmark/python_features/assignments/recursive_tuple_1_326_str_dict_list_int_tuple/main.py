# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'hfeaa'


def func2():
    return {'jipic': 76, 'uzfdr': 79, 'wthkn': 79}


def func3():
    return [26, 56, 99]


def func4():
    return 94


def func5():
    return (6, 59, 93)


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
