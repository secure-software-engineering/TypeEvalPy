# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 19


def func2():
    return (100, 41, 16)


def func3():
    return {'arsfo': 86, 'igbhf': 10, 'fosyu': 74}


def func4():
    return [83, 54, 88]


def func5():
    return 'tiifu'


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
