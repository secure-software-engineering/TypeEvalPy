# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'eulan': 55, 'sznrz': 10, 'rmmhi': 94}


def func2():
    return [72, 71, 35]


def func3():
    return 67.67


def func4():
    return 33


def func5():
    return (5, 29, 95)


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
