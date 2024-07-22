# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'djxvg'


def func2():
    return [29, 78, 98]


def func3():
    return {'yisuu': 74, 'hnzhs': 82, 'tmhgj': 8}


def func4():
    return 26.74


def func5():
    return 30


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
