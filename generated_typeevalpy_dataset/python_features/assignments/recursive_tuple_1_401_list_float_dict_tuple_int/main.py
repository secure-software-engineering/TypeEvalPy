# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [57, 13, 66]


def func2():
    return 88.62


def func3():
    return {'dqgsf': 91, 'pcpev': 21, 'arriv': 80}


def func4():
    return (64, 12, 36)


def func5():
    return 31


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
