# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'nxkzs'


def func2():
    return 71.63


def func3():
    return (45, 44, 90)


def func4():
    return {'pbwjj': 81, 'zynkh': 19, 'gqsfl': 80}


def func5():
    return [91, 62, 12]


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
