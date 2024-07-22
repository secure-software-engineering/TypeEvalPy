# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [61, 82, 4]


def func2():
    return {'cymzl': 50, 'ogjgx': 82, 'lczch': 96}


def func3():
    return (18, 24, 25)


def func4():
    return 67.63


def func5():
    return 'vaofx'


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
