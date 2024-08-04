# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ejdkx': 99, 'jcvdr': 53, 'oydhb': 28}


def func2():
    return 5.16


def func3():
    return 76


def func4():
    return (41, 41, 97)


def func5():
    return 'rpggr'


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
