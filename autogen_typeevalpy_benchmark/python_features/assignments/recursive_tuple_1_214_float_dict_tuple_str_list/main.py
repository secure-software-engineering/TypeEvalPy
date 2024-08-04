# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 30.71


def func2():
    return {'poeet': 34, 'uwpey': 61, 'zquuh': 39}


def func3():
    return (48, 19, 40)


def func4():
    return 'ijtll'


def func5():
    return [51, 98, 54]


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
