# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 95.36


def func2():
    return (32, 31, 100)


def func3():
    return 57


def func4():
    return [84, 65, 77]


def func5():
    return {'iwgxw': 48, 'azrex': 1, 'dtfme': 6}


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
