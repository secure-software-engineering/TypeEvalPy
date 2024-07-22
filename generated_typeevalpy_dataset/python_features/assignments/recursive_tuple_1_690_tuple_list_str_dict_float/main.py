# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (81, 29, 38)


def func2():
    return [70, 79, 36]


def func3():
    return 'hyduk'


def func4():
    return {'tcdrb': 100, 'sdtgb': 81, 'mjzid': 89}


def func5():
    return 70.51


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
