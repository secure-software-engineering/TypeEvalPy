# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 42


def func2():
    return [38, 91, 96]


def func3():
    return {'ayoip': 72, 'cpsqm': 31, 'txhhj': 6}


def func4():
    return (68, 71, 47)


def func5():
    return 'sgxvi'


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
