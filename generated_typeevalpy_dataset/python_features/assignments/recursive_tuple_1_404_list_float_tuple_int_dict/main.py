# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [61, 3, 32]


def func2():
    return 94.84


def func3():
    return (84, 50, 73)


def func4():
    return 46


def func5():
    return {'hsyia': 82, 'gmpai': 4, 'wprii': 61}


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
