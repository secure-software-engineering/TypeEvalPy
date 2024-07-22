# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 35


def func2():
    return (28, 18, 8)


def func3():
    return {'tbdpe': 57, 'utezg': 84, 'gkjcd': 84}


def func4():
    return 'fafhh'


def func5():
    return [96, 99, 66]


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
