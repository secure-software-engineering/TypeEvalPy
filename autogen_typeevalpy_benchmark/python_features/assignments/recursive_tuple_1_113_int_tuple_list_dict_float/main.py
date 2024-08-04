# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 48


def func2():
    return (29, 65, 37)


def func3():
    return [35, 85, 34]


def func4():
    return {'hxxra': 56, 'xaauv': 31, 'ntieo': 72}


def func5():
    return 97.38


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
