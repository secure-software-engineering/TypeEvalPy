# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'lsonf': 100, 'cqcbs': 88, 'ntcyk': 11}


def func2():
    return 'ffjqw'


def func3():
    return 22.57


def func4():
    return (18, 26, 32)


def func5():
    return [40, 86, 44]


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
