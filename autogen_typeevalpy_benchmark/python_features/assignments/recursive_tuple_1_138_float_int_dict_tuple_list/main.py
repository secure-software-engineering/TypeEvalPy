# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 96.76


def func2():
    return 18


def func3():
    return {'frwhi': 61, 'zamrc': 4, 'apdcf': 65}


def func4():
    return (57, 51, 8)


def func5():
    return [16, 39, 52]


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
