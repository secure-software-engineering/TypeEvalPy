# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 60.1


def func2():
    return {'njrza': 64, 'xegjn': 25, 'apkcf': 6}


def func3():
    return 28


def func4():
    return 'hcjed'


def func5():
    return (40, 50, 87)


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
