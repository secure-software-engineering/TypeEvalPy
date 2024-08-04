# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'rwsce'


def func2():
    return (96, 82, 75)


def func3():
    return [11, 11, 89]


def func4():
    return 19.85


def func5():
    return {'ycuoj': 38, 'utpsz': 34, 'irunh': 21}


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
