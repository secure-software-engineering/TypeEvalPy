# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 83.57


def func2():
    return [16, 8, 57]


def func3():
    return {'qbcoz': 67, 'fpavw': 2, 'isxpy': 86}


def func4():
    return (52, 54, 86)


def func5():
    return 86


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
