# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (88, 67, 77)


def func2():
    return 'matxj'


def func3():
    return 15.08


def func4():
    return {'ckiri': 97, 'xphtr': 88, 'acawe': 85}


def func5():
    return 12


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
