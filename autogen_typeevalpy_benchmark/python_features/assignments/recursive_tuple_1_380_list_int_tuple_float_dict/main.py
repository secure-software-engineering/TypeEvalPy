# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [80, 95, 51]


def func2():
    return 56


def func3():
    return (63, 72, 15)


def func4():
    return 9.35


def func5():
    return {'cdosx': 38, 'hiemv': 10, 'dfgpm': 18}


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
