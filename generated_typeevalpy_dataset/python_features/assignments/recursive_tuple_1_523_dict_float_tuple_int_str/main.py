# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'gdfwi': 40, 'srpbv': 16, 'wvxvd': 51}


def func2():
    return 16.96


def func3():
    return (57, 72, 40)


def func4():
    return 77


def func5():
    return 'dyvrx'


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
