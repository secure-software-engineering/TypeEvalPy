# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 50.18


def func2():
    return 'dqcns'


def func3():
    return (28, 1, 56)


def func4():
    return {'bofek': 63, 'gjpqm': 63, 'rehgh': 81}


def func5():
    return [51, 77, 46]


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
