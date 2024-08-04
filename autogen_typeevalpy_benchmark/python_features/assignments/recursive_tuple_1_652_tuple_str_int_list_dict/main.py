# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (17, 27, 58)


def func2():
    return 'nomio'


def func3():
    return 38


def func4():
    return [9, 50, 67]


def func5():
    return {'bszfs': 66, 'ojhto': 55, 'nwhar': 88}


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
