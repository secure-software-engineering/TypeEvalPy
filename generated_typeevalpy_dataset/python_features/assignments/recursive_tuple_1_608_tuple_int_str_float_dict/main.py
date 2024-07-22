# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (70, 36, 56)


def func2():
    return 13


def func3():
    return 'ownhg'


def func4():
    return 13.75


def func5():
    return {'dvnde': 97, 'ryxwx': 89, 'sjfzn': 16}


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
