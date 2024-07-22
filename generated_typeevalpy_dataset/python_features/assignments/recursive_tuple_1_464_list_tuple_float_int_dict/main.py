# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [41, 4, 51]


def func2():
    return (65, 33, 23)


def func3():
    return 88.81


def func4():
    return 96


def func5():
    return {'niqob': 47, 'totfo': 81, 'rluux': 12}


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
