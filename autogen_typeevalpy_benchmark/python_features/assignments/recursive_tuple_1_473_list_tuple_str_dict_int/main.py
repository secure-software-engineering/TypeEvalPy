# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [50, 30, 90]


def func2():
    return (51, 20, 11)


def func3():
    return 'oujbp'


def func4():
    return {'uuhaz': 25, 'kfhus': 17, 'oihpe': 22}


def func5():
    return 50


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
