# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'lrfbi'


def func2():
    return [86, 96, 93]


def func3():
    return {'nhitq': 1, 'jdugk': 40, 'onpjl': 6}


def func4():
    return (61, 13, 79)


def func5():
    return 36


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