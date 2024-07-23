# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (53, 40, 48)


def func2():
    return {'kfdpf': 93, 'rsjti': 3, 'glsoc': 73}


def func3():
    return 65


def func4():
    return [88, 30, 2]


def func5():
    return 'eotif'


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
