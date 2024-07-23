# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 47


def func2():
    return {'vymow': 5, 'iutfh': 69, 'pepln': 58}


def func3():
    return 'bcnrf'


def func4():
    return [24, 34, 81]


def func5():
    return 46.25


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
