# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 44


def func2():
    return 78.7


def func3():
    return 'uuoxw'


def func4():
    return {'wpcby': 22, 'uztzu': 81, 'pwcon': 16}


def func5():
    return (27, 47, 21)


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
