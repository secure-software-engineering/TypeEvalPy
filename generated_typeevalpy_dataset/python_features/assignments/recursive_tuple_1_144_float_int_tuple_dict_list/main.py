# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 56.81


def func2():
    return 95


def func3():
    return (78, 15, 8)


def func4():
    return {'nuqvc': 59, 'pupad': 94, 'cnbnw': 66}


def func5():
    return [90, 23, 4]


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
