# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 30.16


def func2():
    return 9


def func3():
    return {'ejfkk': 62, 'scuxz': 36, 'jmtli': 25}


def func4():
    return (11, 2, 69)


def func5():
    return 'ujkjm'


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
