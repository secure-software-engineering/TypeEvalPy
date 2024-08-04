# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 14


def func2():
    return {'nvdxa': 15, 'ldrfw': 29, 'kwvce': 14}


def func3():
    return (37, 46, 10)


def func4():
    return 61.95


def func5():
    return [16, 47, 11]


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
