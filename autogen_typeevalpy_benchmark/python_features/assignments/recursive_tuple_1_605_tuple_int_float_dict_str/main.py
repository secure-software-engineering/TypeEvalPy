# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (4, 6, 34)


def func2():
    return 86


def func3():
    return 56.14


def func4():
    return {'rulkn': 80, 'ytckj': 49, 'waqcf': 36}


def func5():
    return 'jgerk'


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
