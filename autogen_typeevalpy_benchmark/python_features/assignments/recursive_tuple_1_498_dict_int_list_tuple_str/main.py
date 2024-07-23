# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'csekc': 60, 'ujlss': 50, 'bdljn': 35}


def func2():
    return 84


def func3():
    return [69, 14, 24]


def func4():
    return (24, 62, 15)


def func5():
    return 'xsecc'


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
