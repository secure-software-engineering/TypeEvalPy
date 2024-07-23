# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 92.74


def func2():
    return {'umwgl': 58, 'zefjk': 42, 'caowh': 72}


def func3():
    return 'modyn'


def func4():
    return [5, 12, 72]


def func5():
    return 22


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
