# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [68, 47, 30]


def func2():
    return (68, 40, 90)


def func3():
    return 'tjtzr'


def func4():
    return 8


def func5():
    return {'totlj': 33, 'zykwj': 91, 'myuak': 26}


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
