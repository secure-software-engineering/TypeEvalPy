# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [89, 64, 3]


def func2():
    return 92.71


def func3():
    return 'kfyqo'


def func4():
    return 94


def func5():
    return {'sstpc': 8, 'xdkto': 47, 'esjgt': 58}


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
