# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'nyexp'


def func2():
    return [61, 24, 100]


def func3():
    return 66.81


def func4():
    return 91


def func5():
    return {'xmodz': 13, 'vnwxu': 63, 'xsdcj': 2}


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
