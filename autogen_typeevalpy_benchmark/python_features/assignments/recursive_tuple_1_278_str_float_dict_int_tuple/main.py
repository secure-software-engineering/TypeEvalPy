# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jlgbz'


def func2():
    return 49.95


def func3():
    return {'yjqtn': 49, 'jxwrf': 76, 'sjbsv': 29}


def func4():
    return 22


def func5():
    return (77, 14, 35)


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
