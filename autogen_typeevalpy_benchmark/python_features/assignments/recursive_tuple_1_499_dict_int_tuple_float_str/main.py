# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'gihgf': 4, 'chrsk': 5, 'trruo': 71}


def func2():
    return 84


def func3():
    return (41, 91, 91)


def func4():
    return 89.82


def func5():
    return 'ohtyd'


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
