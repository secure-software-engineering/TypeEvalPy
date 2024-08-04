# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kazpt': 32, 'owgra': 74, 'urjlr': 47}


def func2():
    return [90, 96, 19]


def func3():
    return 'cbdkh'


def func4():
    return (19, 50, 10)


def func5():
    return 1.44


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
