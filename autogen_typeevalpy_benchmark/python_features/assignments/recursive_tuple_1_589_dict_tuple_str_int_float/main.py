# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'becjf': 57, 'iacfu': 63, 'cqhrb': 76}


def func2():
    return (60, 82, 18)


def func3():
    return 'gpdsg'


def func4():
    return 17


def func5():
    return 16.18


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
