# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'lmmpm'


def func2():
    return (30, 69, 89)


def func3():
    return {'uamay': 37, 'bfstk': 22, 'itrzt': 20}


def func4():
    return 28.13


def func5():
    return [82, 56, 20]


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
