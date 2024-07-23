# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (79, 3, 12)


def func2():
    return {'gxont': 6, 'ejzxd': 57, 'ypfml': 89}


def func3():
    return 'qkdqt'


def func4():
    return [70, 59, 10]


def func5():
    return 62.82


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
