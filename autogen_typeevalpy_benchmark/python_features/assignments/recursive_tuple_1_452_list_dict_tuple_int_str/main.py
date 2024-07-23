# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return [67, 97, 57]


def func2():
    return {'aplhi': 49, 'egreq': 26, 'uowma': 92}


def func3():
    return (50, 45, 92)


def func4():
    return 80


def func5():
    return 'tcyoa'


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
