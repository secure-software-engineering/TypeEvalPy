# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'jiwqi': 5, 'hlrbd': 21, 'uzmrh': 20}


def func2():
    return (20, 40, 47)


def func3():
    return [80, 95, 73]


def func4():
    return 'jsfdj'


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
