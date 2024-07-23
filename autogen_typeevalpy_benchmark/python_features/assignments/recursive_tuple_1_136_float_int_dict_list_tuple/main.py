# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 88.95


def func2():
    return 71


def func3():
    return {'kjcks': 64, 'spiva': 68, 'ucrpe': 20}


def func4():
    return [60, 20, 62]


def func5():
    return (59, 35, 63)


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
