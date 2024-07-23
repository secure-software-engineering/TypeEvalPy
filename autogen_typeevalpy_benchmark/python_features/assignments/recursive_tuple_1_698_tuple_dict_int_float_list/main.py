# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (7, 74, 41)


def func2():
    return {'dvvza': 23, 'zrpqd': 46, 'gxhok': 78}


def func3():
    return 18


def func4():
    return 20.89


def func5():
    return [73, 5, 94]


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
