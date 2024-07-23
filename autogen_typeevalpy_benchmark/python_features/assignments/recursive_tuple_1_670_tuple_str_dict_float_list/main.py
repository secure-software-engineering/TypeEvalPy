# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (55, 99, 71)


def func2():
    return 'vmyvr'


def func3():
    return {'nrwhx': 69, 'nitpw': 15, 'ifyns': 39}


def func4():
    return 54.83


def func5():
    return [20, 88, 19]


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
