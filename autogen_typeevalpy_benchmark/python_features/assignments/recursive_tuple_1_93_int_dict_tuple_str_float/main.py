# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 6


def func2():
    return {'penpr': 92, 'drhvj': 10, 'cxryv': 1}


def func3():
    return (20, 100, 84)


def func4():
    return 'ddluz'


def func5():
    return 81.65


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
