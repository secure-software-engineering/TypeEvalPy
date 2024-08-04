# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [86, 42, 18]


def func2():
    return 15.86


def func3():
    return (37, 49, 17)


def func4():
    return {'avfwz': 100, 'jjuvt': 89, 'aysoi': 75}


def func5():
    return 64


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
