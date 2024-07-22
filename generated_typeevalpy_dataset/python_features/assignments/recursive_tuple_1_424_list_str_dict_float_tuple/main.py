# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [20, 86, 59]


def func2():
    return 'asavk'


def func3():
    return {'jnlmk': 11, 'exfqf': 25, 'dmden': 15}


def func4():
    return 51.49


def func5():
    return (83, 30, 10)


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
