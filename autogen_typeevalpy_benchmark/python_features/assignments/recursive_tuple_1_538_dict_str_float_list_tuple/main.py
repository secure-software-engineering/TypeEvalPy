# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'wqwqi': 84, 'hqvwz': 9, 'aecmt': 90}


def func2():
    return 'yckln'


def func3():
    return 66.71


def func4():
    return [48, 62, 31]


def func5():
    return (48, 37, 58)


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
