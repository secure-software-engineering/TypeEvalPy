# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'vbvsl': 48, 'qvleq': 3, 'jfmqq': 58}


def func2():
    return (93, 1, 65)


def func3():
    return 86.06


def func4():
    return 56


def func5():
    return 'hatzt'


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
