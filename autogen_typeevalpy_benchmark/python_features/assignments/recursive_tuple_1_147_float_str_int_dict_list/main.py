# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 7.73


def func2():
    return 'wzbow'


def func3():
    return 79


def func4():
    return {'nkbsc': 94, 'mxgai': 43, 'gitdo': 97}


def func5():
    return [85, 8, 31]


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
