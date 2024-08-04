# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (41, 26, 76)


def func2():
    return 'nzwoq'


def func3():
    return [6, 58, 96]


def func4():
    return {'fnjbm': 66, 'bpjzt': 57, 'qevfg': 53}


def func5():
    return 27


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
