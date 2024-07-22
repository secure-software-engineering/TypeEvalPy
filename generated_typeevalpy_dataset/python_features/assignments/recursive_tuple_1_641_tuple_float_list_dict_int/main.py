# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (37, 90, 44)


def func2():
    return 78.62


def func3():
    return [98, 50, 19]


def func4():
    return {'qwqed': 28, 'whoqg': 41, 'tzmfk': 42}


def func5():
    return 41


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
