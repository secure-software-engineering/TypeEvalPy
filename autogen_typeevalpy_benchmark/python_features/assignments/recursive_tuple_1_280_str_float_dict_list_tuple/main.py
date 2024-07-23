# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ppwpp'


def func2():
    return 25.0


def func3():
    return {'bxheb': 47, 'wjxgu': 20, 'hdlim': 9}


def func4():
    return [2, 60, 24]


def func5():
    return (15, 95, 11)


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
