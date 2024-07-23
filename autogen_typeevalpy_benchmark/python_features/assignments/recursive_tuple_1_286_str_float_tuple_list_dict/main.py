# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kwcxg'


def func2():
    return 57.58


def func3():
    return (24, 31, 76)


def func4():
    return [59, 92, 45]


def func5():
    return {'ftnls': 13, 'ekjmx': 19, 'kqcsv': 55}


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
