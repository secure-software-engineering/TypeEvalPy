# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (42, 62, 13)


def func2():
    return {'wwudw': 67, 'ucryv': 72, 'zhmwe': 84}


def func3():
    return 12


def func4():
    return 29.64


def func5():
    return [16, 17, 69]


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
