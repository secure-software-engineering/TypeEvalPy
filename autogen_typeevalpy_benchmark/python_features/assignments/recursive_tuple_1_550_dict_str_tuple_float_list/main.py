# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'mvsaz': 69, 'dyvjo': 75, 'cacoc': 12}


def func2():
    return 'elwzs'


def func3():
    return (94, 78, 69)


def func4():
    return 88.6


def func5():
    return [33, 62, 72]


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
