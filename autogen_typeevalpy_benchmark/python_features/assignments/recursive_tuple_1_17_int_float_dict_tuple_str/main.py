# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 12


def func2():
    return 16.27


def func3():
    return {'yrbye': 77, 'shcdx': 76, 'gyxbg': 31}


def func4():
    return (64, 66, 97)


def func5():
    return 'nyhio'


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
