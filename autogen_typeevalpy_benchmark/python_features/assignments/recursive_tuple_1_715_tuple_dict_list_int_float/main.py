# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (95, 14, 3)


def func2():
    return {'hueqf': 73, 'kslaf': 18, 'ixsxj': 68}


def func3():
    return [8, 85, 23]


def func4():
    return 78


def func5():
    return 21.2


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
