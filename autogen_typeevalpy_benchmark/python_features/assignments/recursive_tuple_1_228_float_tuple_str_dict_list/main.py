# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 47.48


def func2():
    return (33, 17, 42)


def func3():
    return 'rjpsm'


def func4():
    return {'twffd': 43, 'yfcck': 91, 'xcfer': 60}


def func5():
    return [86, 76, 67]


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
