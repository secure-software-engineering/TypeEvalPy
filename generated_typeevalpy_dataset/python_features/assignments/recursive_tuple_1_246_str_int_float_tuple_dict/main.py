# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'jobcy'


def func2():
    return 70


def func3():
    return 50.73


def func4():
    return (8, 50, 17)


def func5():
    return {'lezob': 14, 'kysxh': 32, 'hfrur': 50}


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
