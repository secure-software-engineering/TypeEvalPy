# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [1, 20, 9]


def func2():
    return 15


def func3():
    return (28, 9, 72)


def func4():
    return {'akwoy': 70, 'cehpp': 14, 'ffrbw': 9}


def func5():
    return 'umaef'


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
