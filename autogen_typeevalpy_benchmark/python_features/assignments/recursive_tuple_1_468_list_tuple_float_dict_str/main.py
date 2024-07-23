# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [92, 37, 55]


def func2():
    return (37, 7, 57)


def func3():
    return 41.2


def func4():
    return {'raalp': 10, 'puqlu': 93, 'octza': 15}


def func5():
    return 'jjjkv'


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
