# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 91


def func2():
    return (73, 85, 8)


def func3():
    return 'yjwfo'


def func4():
    return [68, 39, 20]


def func5():
    return {'wmphs': 72, 'tfuev': 95, 'emieu': 21}


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
