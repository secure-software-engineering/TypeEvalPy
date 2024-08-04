# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (26, 32, 93)


def func2():
    return [10, 48, 34]


def func3():
    return 18.74


def func4():
    return {'taaeb': 95, 'yliqy': 13, 'xaive': 13}


def func5():
    return 'hdkmc'


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
