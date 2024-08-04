# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [12, 22, 76]


def func2():
    return (95, 76, 99)


def func3():
    return 42.93


def func4():
    return 22


def func5():
    return {'kgvku': 17, 'easlj': 1, 'egzxs': 57}


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
