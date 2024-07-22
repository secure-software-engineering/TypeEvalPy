# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (3, 94, 86)


def func2():
    return 8


def func3():
    return 'sfkke'


def func4():
    return {'fylie': 76, 'xpeba': 88, 'sfnpi': 28}


def func5():
    return 94.84


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
