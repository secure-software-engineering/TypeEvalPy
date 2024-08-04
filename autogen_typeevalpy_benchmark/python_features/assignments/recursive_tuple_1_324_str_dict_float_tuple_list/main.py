# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'abwdz'


def func2():
    return {'dshii': 84, 'gmkyr': 5, 'rshsx': 47}


def func3():
    return 16.5


def func4():
    return (25, 45, 9)


def func5():
    return [7, 5, 33]


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
