# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'iekvd'


def func2():
    return {'ecozw': 83, 'ahiup': 24, 'onwuw': 4}


def func3():
    return 29


def func4():
    return [90, 55, 45]


def func5():
    return (35, 3, 41)


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
