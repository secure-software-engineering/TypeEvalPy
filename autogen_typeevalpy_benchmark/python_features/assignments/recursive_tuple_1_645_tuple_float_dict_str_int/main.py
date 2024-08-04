# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (89, 44, 17)


def func2():
    return 89.77


def func3():
    return {'byiop': 98, 'bofas': 56, 'khgre': 81}


def func4():
    return 'sddlm'


def func5():
    return 27


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
