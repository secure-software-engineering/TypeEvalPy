# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 29.79


def func2():
    return 5


def func3():
    return {'mjvqk': 26, 'zcghi': 33, 'oripr': 18}


def func4():
    return [54, 71, 26]


def func5():
    return 'hcoqo'


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
