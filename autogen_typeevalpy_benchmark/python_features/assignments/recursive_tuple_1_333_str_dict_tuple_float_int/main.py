# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'oukax'


def func2():
    return {'efimk': 30, 'aecwv': 10, 'mqmsu': 55}


def func3():
    return (85, 19, 91)


def func4():
    return 55.9


def func5():
    return 61


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
