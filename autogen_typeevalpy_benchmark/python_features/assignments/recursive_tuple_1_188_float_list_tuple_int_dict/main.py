# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 72.52


def func2():
    return [42, 7, 31]


def func3():
    return (69, 31, 39)


def func4():
    return 48


def func5():
    return {'lwylx': 73, 'qakml': 57, 'ixecs': 41}


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
