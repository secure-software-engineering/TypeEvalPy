# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'nbcuo': 22, 'lzmam': 70, 'lcoer': 83}


def func2():
    return 'hnche'


def func3():
    return (90, 23, 67)


def func4():
    return 29


def func5():
    return [82, 99, 1]


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
