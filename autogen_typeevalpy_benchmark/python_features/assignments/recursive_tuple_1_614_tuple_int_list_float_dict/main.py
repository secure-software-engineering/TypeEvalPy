# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (25, 56, 39)


def func2():
    return 23


def func3():
    return [84, 16, 37]


def func4():
    return 10.07


def func5():
    return {'dwvud': 14, 'ctxrn': 38, 'ajkhy': 34}


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
