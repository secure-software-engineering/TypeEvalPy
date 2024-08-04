# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 37


def func2():
    return 'qxjvu'


def func3():
    return {'kvwke': 81, 'qlkrs': 69, 'csbxe': 38}


def func4():
    return (86, 9, 90)


def func5():
    return [93, 93, 28]


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
