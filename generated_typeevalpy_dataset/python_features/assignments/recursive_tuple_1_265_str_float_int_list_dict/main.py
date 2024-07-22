# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'sxoch'


def func2():
    return 33.53


def func3():
    return 34


def func4():
    return [99, 88, 48]


def func5():
    return {'xmgjd': 63, 'lchov': 75, 'hdnwv': 1}


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
