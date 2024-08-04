# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 18.56


def func2():
    return (2, 17, 67)


def func3():
    return 'estbu'


def func4():
    return [95, 85, 38]


def func5():
    return {'jkeey': 34, 'ztvew': 80, 'cemhq': 42}


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
