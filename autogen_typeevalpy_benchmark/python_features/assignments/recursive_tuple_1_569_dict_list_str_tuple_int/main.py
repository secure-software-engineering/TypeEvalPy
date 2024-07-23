# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'frflu': 96, 'fjhkl': 36, 'wzizs': 84}


def func2():
    return [97, 48, 19]


def func3():
    return 'ugooy'


def func4():
    return (7, 34, 18)


def func5():
    return 21


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
