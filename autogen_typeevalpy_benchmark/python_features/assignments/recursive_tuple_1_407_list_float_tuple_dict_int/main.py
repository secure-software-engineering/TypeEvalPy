# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [27, 49, 25]


def func2():
    return 6.19


def func3():
    return (22, 14, 36)


def func4():
    return {'flwan': 77, 'jdfqi': 98, 'gqlrq': 45}


def func5():
    return 93


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
