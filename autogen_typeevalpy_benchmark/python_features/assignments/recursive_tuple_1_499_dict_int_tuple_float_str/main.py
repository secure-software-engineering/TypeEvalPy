# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'nagar': 99, 'pkvqv': 26, 'dashm': 99}


def func2():
    return 58


def func3():
    return (29, 19, 37)


def func4():
    return 30.06


def func5():
    return 'rbgcl'


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
