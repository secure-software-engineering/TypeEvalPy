# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'zwivm': 55, 'itslz': 27, 'qpemr': 37}


def func2():
    return [3, 29, 25]


def func3():
    return 7.01


def func4():
    return 'gymeg'


def func5():
    return 73


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
