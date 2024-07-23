# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 36


def func2():
    return 65.54


def func3():
    return (69, 7, 31)


def func4():
    return {'sevlt': 59, 'jmvok': 61, 'bqzgy': 45}


def func5():
    return [30, 73, 40]


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
