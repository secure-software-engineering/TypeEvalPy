# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 25


def func2():
    return [29, 1, 15]


def func3():
    return (20, 13, 30)


def func4():
    return 'pbtna'


def func5():
    return {'xuluk': 6, 'qiual': 89, 'hlxlz': 52}


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
