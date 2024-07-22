# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 56


def func2():
    return {'xlqdy': 76, 'nyogm': 91, 'uclcn': 13}


def func3():
    return (15, 9, 65)


def func4():
    return [64, 93, 26]


def func5():
    return 89.79


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
