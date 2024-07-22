# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [97, 23, 2]


def func2():
    return 17.05


def func3():
    return 'ryxri'


def func4():
    return (55, 7, 59)


def func5():
    return {'mpsfp': 31, 'xydjv': 71, 'xfvfe': 42}


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
