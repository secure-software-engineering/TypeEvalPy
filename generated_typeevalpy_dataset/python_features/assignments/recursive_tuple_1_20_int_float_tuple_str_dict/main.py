# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 32


def func2():
    return 80.81


def func3():
    return (85, 96, 77)


def func4():
    return 'quisn'


def func5():
    return {'csvat': 97, 'rnuqt': 49, 'afnuo': 61}


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
