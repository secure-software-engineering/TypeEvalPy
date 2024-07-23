# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'fdvic': 14, 'jiuju': 66, 'hzvij': 27}


def func2():
    return 7


def func3():
    return [48, 63, 34]


def func4():
    return 76.57


def func5():
    return 'grugu'


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
