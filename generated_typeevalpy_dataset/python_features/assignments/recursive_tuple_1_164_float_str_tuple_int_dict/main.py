# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 38.65


def func2():
    return 'bdqwf'


def func3():
    return (96, 45, 94)


def func4():
    return 73


def func5():
    return {'wnopy': 78, 'difiv': 20, 'ranlj': 28}


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
