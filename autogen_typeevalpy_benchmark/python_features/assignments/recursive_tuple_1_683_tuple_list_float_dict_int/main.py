# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (3, 86, 47)


def func2():
    return [7, 58, 85]


def func3():
    return 55.48


def func4():
    return {'fwryv': 22, 'yvmxh': 34, 'jmwbx': 89}


def func5():
    return 62


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
