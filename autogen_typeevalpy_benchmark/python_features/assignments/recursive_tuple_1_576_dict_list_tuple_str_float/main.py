# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kdlov': 91, 'zlldl': 27, 'xrdyw': 44}


def func2():
    return [27, 94, 71]


def func3():
    return (52, 61, 54)


def func4():
    return 'rjdxl'


def func5():
    return 50.89


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
