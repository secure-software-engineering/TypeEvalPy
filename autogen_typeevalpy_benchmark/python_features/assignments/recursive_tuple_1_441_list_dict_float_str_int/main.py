# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [19, 62, 57]


def func2():
    return {'xgiie': 31, 'pylrz': 26, 'szbkk': 57}


def func3():
    return 90.76


def func4():
    return 'fioyl'


def func5():
    return 25


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
