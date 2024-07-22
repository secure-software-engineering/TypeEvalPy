# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jpdfi': 2, 'rvwxr': 17, 'votmh': 74}


def func2():
    return 59.22


def func3():
    return [63, 90, 83]


def func4():
    return 'ucwox'


def func5():
    return (62, 7, 42)


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
