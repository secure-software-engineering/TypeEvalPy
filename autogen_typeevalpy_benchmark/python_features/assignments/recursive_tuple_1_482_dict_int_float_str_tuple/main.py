# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cvydb': 77, 'zuamf': 92, 'wnqcr': 38}


def func2():
    return 79


def func3():
    return 52.16


def func4():
    return 'hpovj'


def func5():
    return (85, 18, 44)


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
