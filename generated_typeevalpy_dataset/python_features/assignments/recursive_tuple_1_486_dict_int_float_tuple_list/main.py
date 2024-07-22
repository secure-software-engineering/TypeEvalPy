# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'dwiqi': 78, 'dmryg': 85, 'opdch': 53}


def func2():
    return 17


def func3():
    return 83.48


def func4():
    return (36, 46, 45)


def func5():
    return [23, 33, 6]


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
