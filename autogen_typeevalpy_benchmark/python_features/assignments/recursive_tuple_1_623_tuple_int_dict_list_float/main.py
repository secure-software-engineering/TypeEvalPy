# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (94, 83, 99)


def func2():
    return 38


def func3():
    return {'wagym': 64, 'defbf': 26, 'rikam': 83}


def func4():
    return [22, 10, 64]


def func5():
    return 99.07


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
