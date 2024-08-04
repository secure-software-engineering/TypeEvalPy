# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 95.45


def func2():
    return (74, 13, 16)


def func3():
    return {'zgpsp': 96, 'vsbql': 100, 'lwaku': 56}


def func4():
    return 'raoay'


def func5():
    return [13, 38, 53]


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
