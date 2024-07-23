# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [37, 11, 91]


def func2():
    return {'jjpaf': 71, 'aijns': 29, 'xtwfm': 85}


def func3():
    return 'igdzi'


def func4():
    return (48, 75, 38)


def func5():
    return 37.38


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
