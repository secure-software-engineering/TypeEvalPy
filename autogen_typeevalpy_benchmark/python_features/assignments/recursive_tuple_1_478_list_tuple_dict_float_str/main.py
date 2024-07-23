# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [76, 2, 39]


def func2():
    return (44, 7, 77)


def func3():
    return {'eifeh': 90, 'wnlbb': 98, 'bdumu': 51}


def func4():
    return 89.02


def func5():
    return 'seqxh'


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
