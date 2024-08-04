# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 50.37


def func2():
    return 36


def func3():
    return 'kdeij'


def func4():
    return [74, 3, 37]


def func5():
    return {'auoam': 39, 'dzann': 36, 'iamvk': 41}


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
