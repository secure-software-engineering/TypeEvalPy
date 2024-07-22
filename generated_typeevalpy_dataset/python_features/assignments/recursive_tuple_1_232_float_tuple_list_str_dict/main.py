# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 25.78


def func2():
    return (79, 58, 38)


def func3():
    return [39, 72, 96]


def func4():
    return 'vpzgf'


def func5():
    return {'qcarm': 90, 'asklc': 81, 'arvuh': 45}


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
