# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 51.63


def func2():
    return 19


def func3():
    return (5, 98, 74)


def func4():
    return [55, 83, 22]


def func5():
    return {'mylfq': 78, 'mkqyw': 25, 'ttqys': 42}


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
