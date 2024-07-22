# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jltwe'


def func2():
    return 4


def func3():
    return [53, 32, 26]


def func4():
    return 67.58


def func5():
    return {'mpfdj': 15, 'khpro': 27, 'lzoea': 57}


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
