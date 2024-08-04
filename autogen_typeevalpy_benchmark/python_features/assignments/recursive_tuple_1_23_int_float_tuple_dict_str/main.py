# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 98


def func2():
    return 28.83


def func3():
    return (91, 46, 25)


def func4():
    return {'cphsg': 73, 'mjhxs': 65, 'ffvkw': 64}


def func5():
    return 'eftrp'


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
