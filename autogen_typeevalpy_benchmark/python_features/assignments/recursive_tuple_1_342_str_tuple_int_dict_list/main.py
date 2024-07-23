# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'eieiv'


def func2():
    return (56, 78, 30)


def func3():
    return 89


def func4():
    return {'ogtku': 39, 'mzqck': 29, 'pijxi': 22}


def func5():
    return [58, 60, 84]


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
