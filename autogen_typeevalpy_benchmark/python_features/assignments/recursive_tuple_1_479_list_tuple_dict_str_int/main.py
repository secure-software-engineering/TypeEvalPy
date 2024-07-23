# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [77, 42, 81]


def func2():
    return (49, 17, 47)


def func3():
    return {'hnmok': 46, 'ksuic': 84, 'ufnsi': 53}


def func4():
    return 'nimpm'


def func5():
    return 10


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
