# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 29


def func2():
    return 44.36


def func3():
    return [82, 22, 87]


def func4():
    return (57, 74, 65)


def func5():
    return {'yduhp': 92, 'gyhnk': 74, 'jssqa': 14}


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
