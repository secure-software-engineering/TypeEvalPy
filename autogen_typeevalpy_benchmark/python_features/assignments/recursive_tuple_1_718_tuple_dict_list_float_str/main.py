# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (50, 26, 67)


def func2():
    return {'dcznv': 18, 'upwtf': 48, 'ozpft': 18}


def func3():
    return [33, 63, 42]


def func4():
    return 39.57


def func5():
    return 'bxiqz'


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
