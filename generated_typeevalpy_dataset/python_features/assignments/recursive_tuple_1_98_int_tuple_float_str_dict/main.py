# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return 8


def func2():
    return (25, 12, 55)


def func3():
    return 73.5


def func4():
    return 'mucsu'


def func5():
    return {'uietg': 84, 'afgen': 44, 'ghbxj': 19}


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
