# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [25, 48, 50]


def func2():
    return {'uhxgo': 83, 'yqqcn': 18, 'bmktw': 25}


def func3():
    return 32.17


def func4():
    return 'kzirc'


def func5():
    return (1, 26, 94)


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
