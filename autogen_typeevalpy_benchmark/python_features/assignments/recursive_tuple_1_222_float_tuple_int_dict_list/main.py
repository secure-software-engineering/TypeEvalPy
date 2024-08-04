# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 31.54


def func2():
    return (13, 4, 69)


def func3():
    return 78


def func4():
    return {'ybdjb': 57, 'wyrfe': 16, 'zgxua': 49}


def func5():
    return [4, 57, 96]


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
