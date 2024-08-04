# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 14


def func2():
    return {'srygq': 56, 'pflif': 48, 'qwkls': 19}


def func3():
    return [62, 12, 64]


def func4():
    return (24, 59, 24)


def func5():
    return 81.74


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
