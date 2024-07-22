# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'voiuv'


def func2():
    return [1, 62, 5]


def func3():
    return (45, 56, 25)


def func4():
    return 60


def func5():
    return {'xeetm': 46, 'oleju': 78, 'yfuvw': 53}


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
