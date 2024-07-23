# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'hikzv': 80, 'zdodh': 13, 'afniy': 92}


def func2():
    return 60.06


def func3():
    return [6, 66, 7]


def func4():
    return 'kqhnl'


def func5():
    return 15


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
