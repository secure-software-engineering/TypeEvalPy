# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 6.6


def func2():
    return 'urchy'


def func3():
    return {'djkiw': 37, 'ygrhv': 1, 'ybbva': 41}


def func4():
    return 57


def func5():
    return (95, 20, 12)


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
