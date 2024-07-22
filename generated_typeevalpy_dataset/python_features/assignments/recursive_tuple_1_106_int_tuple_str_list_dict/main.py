# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 14


def func2():
    return (71, 5, 62)


def func3():
    return 'bkkhv'


def func4():
    return [42, 95, 89]


def func5():
    return {'pzswt': 81, 'wgkuw': 32, 'ifjco': 48}


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
