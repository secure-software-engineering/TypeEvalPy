# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'uvtnf'


def func2():
    return (15, 37, 19)


def func3():
    return 37


def func4():
    return [36, 23, 55]


def func5():
    return {'tmtbl': 100, 'hffwv': 31, 'zhmld': 83}


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
