# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'iofrc'


def func2():
    return {'qyadt': 70, 'grrkx': 89, 'fecyi': 71}


def func3():
    return [82, 9, 10]


def func4():
    return (20, 16, 1)


def func5():
    return 31


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
