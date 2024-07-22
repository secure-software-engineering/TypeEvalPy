# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 58.05


def func2():
    return [98, 22, 29]


def func3():
    return (27, 56, 40)


def func4():
    return {'ttbsr': 69, 'ajntg': 14, 'gozgh': 57}


def func5():
    return 'ayzbl'


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
