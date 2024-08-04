# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return (72, 80, 52)


def func2():
    return 17


def func3():
    return {'xozux': 58, 'zazjn': 79, 'wcrgy': 53}


def func4():
    return 'kylim'


def func5():
    return [97, 98, 84]


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
