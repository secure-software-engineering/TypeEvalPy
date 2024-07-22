# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'uneni': 81, 'rayry': 18, 'sbcjo': 100}


def func2():
    return (2, 56, 70)


def func3():
    return 92.14


def func4():
    return [19, 94, 6]


def func5():
    return 88


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
