# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 22


def func2():
    return 'sbnvi'


def func3():
    return (81, 25, 80)


def func4():
    return {'foydf': 9, 'jekik': 28, 'lbvqj': 53}


def func5():
    return 30.85


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
