# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'okihf': 88, 'qkdnu': 66, 'dispr': 63}


def func2():
    return 98


def func3():
    return 'ntrqi'


def func4():
    return [83, 97, 94]


def func5():
    return 77.48


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
