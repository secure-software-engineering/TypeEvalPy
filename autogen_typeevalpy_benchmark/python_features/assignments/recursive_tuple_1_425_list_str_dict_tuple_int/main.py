# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [27, 92, 53]


def func2():
    return 'cfsxi'


def func3():
    return {'zbgoc': 41, 'ivaex': 84, 'hhddc': 5}


def func4():
    return (25, 90, 38)


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
