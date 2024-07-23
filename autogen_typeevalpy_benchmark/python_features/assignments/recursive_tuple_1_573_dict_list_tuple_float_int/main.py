# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'vbuiz': 33, 'sqzco': 89, 'mfyml': 38}


def func2():
    return [21, 52, 6]


def func3():
    return (22, 100, 60)


def func4():
    return 93.67


def func5():
    return 48


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
