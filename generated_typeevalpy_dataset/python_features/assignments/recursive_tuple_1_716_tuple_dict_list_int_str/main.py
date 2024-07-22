# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (85, 72, 28)


def func2():
    return {'fxled': 5, 'eztdc': 1, 'sfjfn': 25}


def func3():
    return [32, 69, 26]


def func4():
    return 47


def func5():
    return 'vlljw'


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
