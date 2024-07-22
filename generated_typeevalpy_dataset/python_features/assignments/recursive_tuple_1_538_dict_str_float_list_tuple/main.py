# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'vkzxt': 76, 'ijsti': 19, 'smqaa': 12}


def func2():
    return 'vmeqp'


def func3():
    return 23.41


def func4():
    return [39, 67, 30]


def func5():
    return (40, 57, 30)


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
