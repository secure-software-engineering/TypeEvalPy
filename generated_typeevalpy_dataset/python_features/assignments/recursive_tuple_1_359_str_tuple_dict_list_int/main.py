# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 'mvunz'


def func2():
    return (42, 63, 26)


def func3():
    return {'mpezy': 20, 'suiom': 84, 'bxmvf': 57}


def func4():
    return [94, 50, 48]


def func5():
    return 18


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
