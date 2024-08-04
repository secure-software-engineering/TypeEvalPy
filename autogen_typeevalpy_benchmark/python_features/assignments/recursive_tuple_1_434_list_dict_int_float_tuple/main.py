# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [10, 19, 94]


def func2():
    return {'cefgt': 22, 'wilss': 48, 'wnljv': 34}


def func3():
    return 66


def func4():
    return 18.31


def func5():
    return (17, 16, 86)


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
