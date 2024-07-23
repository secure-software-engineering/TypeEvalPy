# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 94.34


def func2():
    return {'yfvrt': 68, 'bpwui': 97, 'zxxcj': 57}


def func3():
    return (3, 40, 46)


def func4():
    return 92


def func5():
    return [88, 37, 87]


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
