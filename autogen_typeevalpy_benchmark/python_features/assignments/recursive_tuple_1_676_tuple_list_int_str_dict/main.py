# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (55, 82, 45)


def func2():
    return [96, 4, 74]


def func3():
    return 93


def func4():
    return 'qjvdx'


def func5():
    return {'kldtz': 17, 'kyazt': 18, 'xhvxd': 88}


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
