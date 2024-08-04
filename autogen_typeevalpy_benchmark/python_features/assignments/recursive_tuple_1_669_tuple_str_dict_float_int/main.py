# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (83, 12, 68)


def func2():
    return 'mpwfh'


def func3():
    return {'vgizn': 42, 'cbbxy': 7, 'qstyz': 26}


def func4():
    return 40.66


def func5():
    return 57


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
