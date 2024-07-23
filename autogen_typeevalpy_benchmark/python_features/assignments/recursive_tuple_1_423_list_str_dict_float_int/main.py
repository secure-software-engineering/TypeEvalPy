# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [97, 26, 50]


def func2():
    return 'rlmty'


def func3():
    return {'kimgy': 74, 'cubvu': 57, 'sekjq': 29}


def func4():
    return 37.82


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
