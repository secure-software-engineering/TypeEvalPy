# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [12, 71, 23]


def func2():
    return 37.39


def func3():
    return 29


def func4():
    return (44, 47, 76)


def func5():
    return {'enead': 57, 'vwlno': 10, 'zyzwh': 20}


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
