# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'bdnqd'


def func2():
    return 97


def func3():
    return [91, 29, 4]


def func4():
    return {'endje': 80, 'pwcyf': 44, 'sqzfc': 66}


def func5():
    return (74, 3, 99)


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
