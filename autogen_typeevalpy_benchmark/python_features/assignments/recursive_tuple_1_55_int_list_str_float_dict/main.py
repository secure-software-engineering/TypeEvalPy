# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 1


def func2():
    return [80, 53, 6]


def func3():
    return 'gbvze'


def func4():
    return 55.27


def func5():
    return {'vgavr': 76, 'ciljc': 14, 'thyes': 64}


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
