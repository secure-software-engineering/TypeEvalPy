# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 74


def func2():
    return 'ebevb'


def func3():
    return (11, 6, 81)


def func4():
    return [41, 19, 95]


def func5():
    return {'cengm': 5, 'wqhop': 63, 'dylxg': 50}


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
