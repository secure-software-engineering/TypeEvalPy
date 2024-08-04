# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [75, 34, 42]


def func2():
    return 'jbmbp'


def func3():
    return (84, 74, 39)


def func4():
    return 80.89


def func5():
    return {'hzgbx': 21, 'zrhxw': 2, 'plkil': 40}


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
