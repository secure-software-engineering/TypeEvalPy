# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 17.84


def func2():
    return {'kbvyt': 90, 'taxot': 33, 'thprn': 77}


def func3():
    return [14, 56, 8]


def func4():
    return (28, 56, 77)


def func5():
    return 'glmah'


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
