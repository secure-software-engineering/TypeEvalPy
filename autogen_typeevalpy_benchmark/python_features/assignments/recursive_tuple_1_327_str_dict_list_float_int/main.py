# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'kfddi'


def func2():
    return {'hdimh': 97, 'xhpuy': 9, 'kgecu': 43}


def func3():
    return [88, 49, 43]


def func4():
    return 90.96


def func5():
    return 37


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
