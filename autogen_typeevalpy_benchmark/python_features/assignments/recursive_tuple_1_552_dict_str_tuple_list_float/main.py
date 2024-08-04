# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'tytyf': 6, 'psdfi': 65, 'fonhy': 21}


def func2():
    return 'donil'


def func3():
    return (19, 92, 2)


def func4():
    return [22, 9, 22]


def func5():
    return 20.73


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
