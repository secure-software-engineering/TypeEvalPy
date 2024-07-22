# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'vcabc': 75, 'ekblp': 36, 'orbuk': 54}


def func2():
    return 8


def func3():
    return 81.26


def func4():
    return 'nwgow'


def func5():
    return (87, 88, 77)


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
