# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ghrpu': 57, 'nbpza': 82, 'asuis': 66}


def func2():
    return (55, 15, 58)


def func3():
    return [77, 51, 26]


def func4():
    return 75


def func5():
    return 70.28


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
