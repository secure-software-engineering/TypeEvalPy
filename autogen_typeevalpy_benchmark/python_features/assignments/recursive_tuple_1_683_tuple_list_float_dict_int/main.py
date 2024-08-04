# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (56, 62, 69)


def func2():
    return [53, 22, 81]


def func3():
    return 11.28


def func4():
    return {'umooc': 19, 'pknld': 55, 'tvkov': 75}


def func5():
    return 85


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
