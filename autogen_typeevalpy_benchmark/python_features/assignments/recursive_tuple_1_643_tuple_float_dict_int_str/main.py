# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (88, 18, 27)


def func2():
    return 56.99


def func3():
    return {'whbwx': 61, 'itvyx': 31, 'lqpee': 80}


def func4():
    return 91


def func5():
    return 'eswqb'


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
