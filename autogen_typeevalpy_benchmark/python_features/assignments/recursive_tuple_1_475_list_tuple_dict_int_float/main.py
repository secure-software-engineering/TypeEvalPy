# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [40, 92, 11]


def func2():
    return (85, 77, 74)


def func3():
    return {'rgfig': 34, 'dzzyz': 26, 'ejbnf': 5}


def func4():
    return 89


def func5():
    return 24.85


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
