# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'bbqwd'


def func2():
    return (79, 48, 30)


def func3():
    return {'tsxlq': 30, 'usjpi': 66, 'orvcj': 12}


def func4():
    return [19, 85, 48]


def func5():
    return 90.92


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
