# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'hexib'


def func2():
    return (79, 17, 56)


def func3():
    return 14


def func4():
    return [10, 57, 68]


def func5():
    return {'quzee': 60, 'rtupx': 26, 'mpitr': 75}


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
