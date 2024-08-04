# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 87.9


def func2():
    return 7


def func3():
    return {'tkkau': 43, 'wlbbv': 8, 'qichm': 16}


def func4():
    return (95, 75, 87)


def func5():
    return 'nssno'


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
