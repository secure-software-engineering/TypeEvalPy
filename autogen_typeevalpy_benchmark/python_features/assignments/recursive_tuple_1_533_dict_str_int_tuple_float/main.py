# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'foqgp': 57, 'lgrab': 32, 'agqdq': 84}


def func2():
    return 'keamu'


def func3():
    return 74


def func4():
    return (69, 41, 98)


def func5():
    return 78.11


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
