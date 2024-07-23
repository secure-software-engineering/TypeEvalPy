# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 91


def func2():
    return {'rijnd': 98, 'awiqz': 6, 'swspq': 11}


def func3():
    return (38, 68, 88)


def func4():
    return [79, 50, 95]


def func5():
    return 47.97


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
