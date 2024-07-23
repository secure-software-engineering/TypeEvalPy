# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'sdadc'


def func2():
    return 91


def func3():
    return [42, 6, 38]


def func4():
    return 23.35


def func5():
    return {'cpumo': 93, 'gswas': 46, 'jxfzj': 5}


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
