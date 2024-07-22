# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'tibhl'


def func2():
    return 41.48


def func3():
    return {'ttmky': 40, 'jrfzi': 50, 'lwspq': 75}


def func4():
    return [42, 53, 55]


def func5():
    return (76, 24, 73)


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
