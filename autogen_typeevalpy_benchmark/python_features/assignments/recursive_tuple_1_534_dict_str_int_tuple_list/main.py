# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'nhyxw': 95, 'izpff': 37, 'aadva': 35}


def func2():
    return 'oafvq'


def func3():
    return 75


def func4():
    return (9, 5, 80)


def func5():
    return [31, 30, 33]


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
