# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'ufthd'


def func2():
    return 94.84


def func3():
    return (91, 61, 72)


def func4():
    return {'mbewk': 83, 'hoqpm': 20, 'ydpdy': 11}


def func5():
    return 64


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
