# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'sgmui'


def func2():
    return (54, 81, 83)


def func3():
    return [23, 39, 65]


def func4():
    return {'crnvd': 57, 'ddnbl': 84, 'fyven': 6}


def func5():
    return 87


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
