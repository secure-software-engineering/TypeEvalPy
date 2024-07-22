# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [89, 66, 47]


def func2():
    return (37, 9, 10)


def func3():
    return 'yfmyc'


def func4():
    return {'wpnne': 50, 'dycyt': 57, 'mufxo': 74}


def func5():
    return 22.39


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
