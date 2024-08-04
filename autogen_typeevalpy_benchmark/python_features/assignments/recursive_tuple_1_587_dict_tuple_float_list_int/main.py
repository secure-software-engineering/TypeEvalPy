# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'dbdzk': 27, 'blphb': 58, 'aeugc': 44}


def func2():
    return (80, 13, 76)


def func3():
    return 14.11


def func4():
    return [51, 58, 10]


def func5():
    return 90


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
