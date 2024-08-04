# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 69.27


def func2():
    return (18, 99, 99)


def func3():
    return 9


def func4():
    return 'wstyj'


def func5():
    return {'utfif': 7, 'jfzgp': 68, 'ydqlu': 8}


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
