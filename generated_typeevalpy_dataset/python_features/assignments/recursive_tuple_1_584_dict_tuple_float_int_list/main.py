# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'duxqi': 46, 'vsegd': 12, 'jbmms': 92}


def func2():
    return (12, 66, 25)


def func3():
    return 17.47


def func4():
    return 24


def func5():
    return [93, 5, 15]


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
