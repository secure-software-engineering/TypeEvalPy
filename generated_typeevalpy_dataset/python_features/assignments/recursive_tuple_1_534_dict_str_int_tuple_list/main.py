# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'elomf': 21, 'rtdof': 63, 'xvvbn': 98}


def func2():
    return 'dozuf'


def func3():
    return 72


def func4():
    return (8, 29, 6)


def func5():
    return [87, 79, 4]


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
