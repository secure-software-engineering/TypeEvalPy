# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (80, 70, 16)


def func2():
    return {'rqgss': 26, 'wjvyt': 39, 'jgxzg': 48}


def func3():
    return 73.13


def func4():
    return 23


def func5():
    return [92, 73, 80]


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
