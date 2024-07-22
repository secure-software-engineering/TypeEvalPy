# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (95, 70, 11)


def func2():
    return {'zinpu': 71, 'mykxh': 19, 'dfiqf': 70}


def func3():
    return 29


def func4():
    return [68, 40, 18]


def func5():
    return 'dkbpe'


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
