# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'djrby': 57, 'fnpsc': 6, 'cqeyu': 92}


def func2():
    return 'skldj'


def func3():
    return 8.05


def func4():
    return 96


def func5():
    return (4, 49, 99)


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
