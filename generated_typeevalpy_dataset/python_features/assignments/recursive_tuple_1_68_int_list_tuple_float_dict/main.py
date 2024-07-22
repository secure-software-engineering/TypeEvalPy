# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 79


def func2():
    return [8, 96, 98]


def func3():
    return (9, 66, 33)


def func4():
    return 10.37


def func5():
    return {'ukkii': 82, 'yhyyw': 57, 'rjlhs': 53}


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
