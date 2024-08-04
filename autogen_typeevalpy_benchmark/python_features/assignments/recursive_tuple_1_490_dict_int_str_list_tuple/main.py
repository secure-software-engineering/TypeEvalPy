# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'onfem': 68, 'mcpud': 69, 'qrays': 80}


def func2():
    return 61


def func3():
    return 'qkgqf'


def func4():
    return [81, 88, 74]


def func5():
    return (90, 89, 40)


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
