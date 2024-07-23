# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (12, 65, 35)


def func2():
    return [12, 43, 7]


def func3():
    return 'dpzko'


def func4():
    return 35.84


def func5():
    return {'mpfrf': 29, 'iefia': 25, 'whgnr': 58}


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
