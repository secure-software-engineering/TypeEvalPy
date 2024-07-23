# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jvhqu': 17, 'jxrzg': 23, 'qmjfm': 57}


def func2():
    return 57.07


def func3():
    return 60


def func4():
    return (18, 70, 18)


def func5():
    return 'fuvax'


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
