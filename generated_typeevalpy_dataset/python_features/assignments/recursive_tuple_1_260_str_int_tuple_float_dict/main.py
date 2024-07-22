# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'yasqn'


def func2():
    return 25


def func3():
    return (65, 3, 55)


def func4():
    return 6.26


def func5():
    return {'bkpus': 78, 'bvcvg': 95, 'ybzwd': 81}


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
