# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (88, 21, 53)


def func2():
    return 38


def func3():
    return 44.92


def func4():
    return 'lzpmp'


def func5():
    return {'zgkbp': 31, 'jpqqk': 14, 'lqreq': 49}


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
