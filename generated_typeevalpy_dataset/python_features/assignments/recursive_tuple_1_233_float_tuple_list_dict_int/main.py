# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 52.75


def func2():
    return (56, 32, 39)


def func3():
    return [54, 40, 88]


def func4():
    return {'nvsbh': 85, 'elvus': 91, 'voijv': 54}


def func5():
    return 46


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
