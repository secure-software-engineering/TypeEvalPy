# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mbxsu': 4, 'nyzpg': 88, 'bijga': 68}


def func2():
    return (78, 99, 19)


def func3():
    return 61


def func4():
    return 20.8


def func5():
    return 'kcxpl'


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
