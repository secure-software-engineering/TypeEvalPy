# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'bsgwi'


def func2():
    return 75.61


def func3():
    return (66, 4, 26)


def func4():
    return 51


def func5():
    return {'awzar': 91, 'xurhw': 20, 'shkzp': 16}


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
