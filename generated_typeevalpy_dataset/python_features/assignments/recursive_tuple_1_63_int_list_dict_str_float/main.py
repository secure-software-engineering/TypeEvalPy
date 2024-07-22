# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70


def func2():
    return [17, 8, 28]


def func3():
    return {'seqvk': 65, 'anttm': 47, 'ezvlz': 99}


def func4():
    return 'rgdsw'


def func5():
    return 53.9


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
