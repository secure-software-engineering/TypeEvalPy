# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'aedzj'


def func2():
    return {'rvjob': 63, 'xibpz': 14, 'pveek': 35}


def func3():
    return 59.74


def func4():
    return [79, 68, 10]


def func5():
    return (79, 37, 18)


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
