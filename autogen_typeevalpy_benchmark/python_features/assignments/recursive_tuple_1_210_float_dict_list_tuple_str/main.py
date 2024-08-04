# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 84.16


def func2():
    return {'vunff': 8, 'rkcib': 58, 'ontwz': 73}


def func3():
    return [67, 32, 32]


def func4():
    return (33, 95, 24)


def func5():
    return 'rqgrl'


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
