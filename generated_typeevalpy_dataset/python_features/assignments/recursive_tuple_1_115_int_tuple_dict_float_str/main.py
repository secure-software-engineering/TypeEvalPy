# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 98


def func2():
    return (45, 88, 77)


def func3():
    return {'obkzz': 91, 'qnrsq': 21, 'dtxvd': 27}


def func4():
    return 65.95


def func5():
    return 'xxdqc'


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
