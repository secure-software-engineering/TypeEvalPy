# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (31, 56, 2)


def func2():
    return 37.73


def func3():
    return 'dnqql'


def func4():
    return {'vqpaf': 26, 'bdeug': 99, 'ajage': 59}


def func5():
    return 97


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
