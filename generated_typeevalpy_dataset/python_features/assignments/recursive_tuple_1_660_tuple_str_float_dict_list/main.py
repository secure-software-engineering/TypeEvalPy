# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (60, 76, 39)


def func2():
    return 'fbfzd'


def func3():
    return 33.41


def func4():
    return {'uheas': 33, 'drrmw': 1, 'wmtqq': 40}


def func5():
    return [44, 44, 93]


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
