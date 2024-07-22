# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 17.89


def func2():
    return 7


def func3():
    return [57, 48, 31]


def func4():
    return (55, 98, 42)


def func5():
    return {'rlfjv': 96, 'szwkv': 19, 'agrru': 2}


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
