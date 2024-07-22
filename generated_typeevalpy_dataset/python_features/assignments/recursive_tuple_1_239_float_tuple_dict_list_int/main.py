# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 7.92


def func2():
    return (12, 78, 61)


def func3():
    return {'uxhua': 95, 'gzhol': 38, 'phmtn': 55}


def func4():
    return [62, 52, 89]


def func5():
    return 96


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
