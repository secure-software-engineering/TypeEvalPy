# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 89


def func2():
    return {'xoxvh': 18, 'zrmvd': 35, 'byldz': 73}


def func3():
    return 73.97


def func4():
    return 'qptxf'


def func5():
    return (35, 91, 6)


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
