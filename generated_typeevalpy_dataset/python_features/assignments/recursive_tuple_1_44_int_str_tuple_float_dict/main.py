# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 95


def func2():
    return 'szdfd'


def func3():
    return (80, 54, 17)


def func4():
    return 30.67


def func5():
    return {'mtcze': 25, 'asjmf': 25, 'hnqnq': 21}


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
