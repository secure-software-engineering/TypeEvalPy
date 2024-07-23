# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ndijz'


def func2():
    return {'dctqs': 17, 'offum': 15, 'cvvby': 72}


def func3():
    return [43, 36, 66]


def func4():
    return (74, 45, 63)


def func5():
    return 34


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
