# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [9, 2, 30]


def func2():
    return 75


def func3():
    return {'yzckt': 70, 'suxqu': 28, 'ncxhm': 97}


def func4():
    return 'kbrle'


def func5():
    return (85, 69, 14)


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
