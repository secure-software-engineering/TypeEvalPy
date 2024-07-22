# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 70


def func2():
    return [75, 65, 75]


def func3():
    return {'kqius': 31, 'ntyok': 3, 'kulrs': 63}


def func4():
    return 25.26


def func5():
    return (61, 62, 4)


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
