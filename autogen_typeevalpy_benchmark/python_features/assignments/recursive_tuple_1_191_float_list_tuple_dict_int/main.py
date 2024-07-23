# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 34.62


def func2():
    return [51, 31, 35]


def func3():
    return (36, 25, 72)


def func4():
    return {'sozmy': 70, 'nogkw': 100, 'wfcfw': 38}


def func5():
    return 37


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
