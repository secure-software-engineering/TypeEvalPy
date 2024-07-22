# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (4, 31, 82)


def func2():
    return 'doapm'


def func3():
    return [32, 21, 15]


def func4():
    return 43


def func5():
    return {'fcyrp': 98, 'qnwtl': 94, 'vrfqc': 21}


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
