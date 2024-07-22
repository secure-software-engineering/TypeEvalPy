# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 56


def func2():
    return (31, 96, 10)


def func3():
    return 61.46


def func4():
    return [32, 36, 13]


def func5():
    return {'ppbml': 42, 'vlbaq': 19, 'ridgf': 46}


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
