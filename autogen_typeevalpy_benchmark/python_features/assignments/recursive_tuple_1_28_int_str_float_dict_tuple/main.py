# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 80


def func2():
    return 'ajuwq'


def func3():
    return 34.62


def func4():
    return {'yulif': 57, 'cpbuf': 24, 'oqgks': 32}


def func5():
    return (18, 6, 8)


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
