# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'crrpq'


def func2():
    return 99


def func3():
    return {'zezit': 2, 'uwapx': 81, 'nfmwl': 87}


def func4():
    return (85, 84, 41)


def func5():
    return [9, 7, 67]


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
