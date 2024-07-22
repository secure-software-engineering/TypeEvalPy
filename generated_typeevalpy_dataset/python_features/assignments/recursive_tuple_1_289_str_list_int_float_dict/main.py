# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'gpksf'


def func2():
    return [92, 98, 2]


def func3():
    return 55


def func4():
    return 81.48


def func5():
    return {'pcrmx': 44, 'iolqg': 4, 'mohxq': 10}


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
