# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'ialew': 84, 'aashl': 3, 'kkzmr': 19}


def func2():
    return 73.63


def func3():
    return [79, 13, 10]


def func4():
    return (88, 63, 33)


def func5():
    return 'hhvze'


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
