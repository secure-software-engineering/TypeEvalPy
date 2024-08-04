# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 47


def func2():
    return {'lsxbk': 95, 'ynaps': 51, 'dbous': 64}


def func3():
    return [88, 69, 66]


def func4():
    return 97.18


def func5():
    return (22, 57, 97)


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
