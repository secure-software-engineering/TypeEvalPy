# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'fbfgd'


def func2():
    return 87.18


def func3():
    return {'nitra': 90, 'tmrso': 11, 'bpfpa': 75}


def func4():
    return (48, 66, 22)


def func5():
    return [51, 28, 20]


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
