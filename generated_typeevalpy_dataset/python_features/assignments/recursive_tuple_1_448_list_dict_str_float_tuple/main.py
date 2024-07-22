# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [6, 40, 100]


def func2():
    return {'uesme': 54, 'dcqbr': 83, 'ylpib': 58}


def func3():
    return 'qwajt'


def func4():
    return 38.57


def func5():
    return (82, 59, 7)


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
