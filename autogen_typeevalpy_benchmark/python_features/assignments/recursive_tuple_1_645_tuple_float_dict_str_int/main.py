# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (54, 50, 36)


def func2():
    return 35.22


def func3():
    return {'npebg': 41, 'ljimc': 1, 'kdwvt': 83}


def func4():
    return 'oqcww'


def func5():
    return 91


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
