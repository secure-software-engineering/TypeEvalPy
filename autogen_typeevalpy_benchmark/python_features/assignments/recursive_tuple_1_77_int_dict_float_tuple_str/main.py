# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 82


def func2():
    return {'csyeb': 87, 'tomwz': 69, 'lntmn': 90}


def func3():
    return 13.34


def func4():
    return (2, 79, 25)


def func5():
    return 'xtsst'


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
