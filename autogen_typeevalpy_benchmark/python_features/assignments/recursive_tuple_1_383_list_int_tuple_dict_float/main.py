# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [57, 12, 46]


def func2():
    return 23


def func3():
    return (31, 70, 52)


def func4():
    return {'lmoze': 70, 'yljcp': 20, 'srlpm': 80}


def func5():
    return 57.88


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
