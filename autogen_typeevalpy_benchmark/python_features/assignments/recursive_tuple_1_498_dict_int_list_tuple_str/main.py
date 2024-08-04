# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'qvzol': 11, 'uxpyg': 10, 'jhgik': 29}


def func2():
    return 70


def func3():
    return [71, 48, 7]


def func4():
    return (27, 38, 24)


def func5():
    return 'ekyta'


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
