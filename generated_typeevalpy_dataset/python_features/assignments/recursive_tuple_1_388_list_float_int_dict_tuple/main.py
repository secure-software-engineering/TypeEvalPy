# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [19, 95, 71]


def func2():
    return 94.97


def func3():
    return 75


def func4():
    return {'zjsrm': 43, 'zdbtm': 68, 'jbpdi': 20}


def func5():
    return (36, 79, 47)


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
