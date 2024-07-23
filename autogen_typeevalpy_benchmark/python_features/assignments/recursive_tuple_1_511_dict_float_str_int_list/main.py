# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'lftch': 60, 'qedvg': 1, 'crmcy': 41}


def func2():
    return 48.1


def func3():
    return 'qkroy'


def func4():
    return 37


def func5():
    return [12, 22, 97]


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
