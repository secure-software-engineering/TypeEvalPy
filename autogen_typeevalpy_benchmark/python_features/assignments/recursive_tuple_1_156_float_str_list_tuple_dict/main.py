# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 4.82


def func2():
    return 'hggqu'


def func3():
    return [2, 16, 40]


def func4():
    return (73, 85, 42)


def func5():
    return {'vwlaa': 57, 'ajqok': 24, 'pcxoy': 34}


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
