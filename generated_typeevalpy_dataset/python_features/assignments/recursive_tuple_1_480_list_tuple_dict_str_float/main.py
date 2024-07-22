# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [24, 56, 84]


def func2():
    return (72, 26, 96)


def func3():
    return {'glvir': 25, 'bomwl': 77, 'hzgkg': 35}


def func4():
    return 'zupfd'


def func5():
    return 69.68


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
