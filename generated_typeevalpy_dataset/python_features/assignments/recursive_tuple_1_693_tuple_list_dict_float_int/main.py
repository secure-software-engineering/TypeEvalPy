# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (12, 52, 23)


def func2():
    return [22, 56, 67]


def func3():
    return {'adgzg': 74, 'hpilu': 13, 'bfdmd': 76}


def func4():
    return 1.9


def func5():
    return 73


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
