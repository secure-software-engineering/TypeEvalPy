# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'xcrnp': 56, 'ofgqs': 12, 'qozzv': 47}


def func2():
    return 'qhrci'


def func3():
    return 39.2


def func4():
    return [49, 31, 75]


def func5():
    return (63, 73, 24)


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
