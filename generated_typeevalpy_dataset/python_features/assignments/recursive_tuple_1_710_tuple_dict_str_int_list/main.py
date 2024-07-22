# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (57, 7, 99)


def func2():
    return {'kcbdk': 56, 'kguue': 38, 'tkldy': 54}


def func3():
    return 'fiwsu'


def func4():
    return 92


def func5():
    return [43, 96, 78]


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
