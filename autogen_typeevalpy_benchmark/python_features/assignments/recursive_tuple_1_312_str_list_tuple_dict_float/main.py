# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'gcbru'


def func2():
    return [95, 23, 37]


def func3():
    return (71, 61, 55)


def func4():
    return {'xgvfs': 32, 'bcved': 2, 'mtsdy': 42}


def func5():
    return 85.69


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
