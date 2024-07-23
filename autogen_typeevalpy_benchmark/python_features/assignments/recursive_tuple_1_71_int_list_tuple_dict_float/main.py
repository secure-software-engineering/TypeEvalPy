# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 66


def func2():
    return [91, 97, 100]


def func3():
    return (44, 88, 94)


def func4():
    return {'kbcsu': 49, 'yzwyz': 59, 'kdwci': 74}


def func5():
    return 5.97


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
