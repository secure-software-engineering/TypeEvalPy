# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fyfmw': 56, 'tifhx': 12, 'lysau': 38}


def func2():
    return [22, 69, 81]


def func3():
    return 5.2


def func4():
    return (67, 2, 90)


def func5():
    return 'luyas'


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
