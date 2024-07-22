# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [96, 45, 4]


def func2():
    return 47.31


def func3():
    return (44, 32, 39)


def func4():
    return 'susbm'


def func5():
    return {'vnsoc': 100, 'jrvre': 79, 'ctfyh': 80}


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
