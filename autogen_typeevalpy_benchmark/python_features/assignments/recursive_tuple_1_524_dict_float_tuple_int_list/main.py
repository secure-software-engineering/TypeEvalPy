# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'rxhlb': 27, 'txxqn': 55, 'ewuaq': 48}


def func2():
    return 88.97


def func3():
    return (16, 7, 30)


def func4():
    return 35


def func5():
    return [38, 39, 33]


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
