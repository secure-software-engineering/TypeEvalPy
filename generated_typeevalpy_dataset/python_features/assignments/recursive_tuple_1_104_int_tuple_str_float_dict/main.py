# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 38


def func2():
    return (81, 95, 52)


def func3():
    return 'ugbqt'


def func4():
    return 70.55


def func5():
    return {'fddnz': 2, 'eamuu': 25, 'goovc': 35}


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
