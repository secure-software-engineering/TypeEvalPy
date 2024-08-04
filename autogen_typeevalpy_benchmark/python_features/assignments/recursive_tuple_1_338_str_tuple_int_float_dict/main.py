# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'bbkzh'


def func2():
    return (15, 74, 1)


def func3():
    return 84


def func4():
    return 21.81


def func5():
    return {'cskil': 19, 'dqdjz': 27, 'jnhrw': 50}


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
