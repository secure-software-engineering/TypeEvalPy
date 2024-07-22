# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'khubz': 23, 'ocspw': 19, 'ygtxq': 58}


def func2():
    return (83, 100, 79)


def func3():
    return 35


def func4():
    return 'fzctb'


def func5():
    return 34.58


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
