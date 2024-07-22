# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'cqfro': 38, 'fzfgx': 100, 'iqmcl': 82}


def func2():
    return [4, 69, 67]


def func3():
    return 16


def func4():
    return 69.51


def func5():
    return (82, 40, 46)


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
