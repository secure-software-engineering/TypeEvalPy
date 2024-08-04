# Three variables are assigned a value via a recursive tuple assignment


def func1():
    return {'kfnya': 26, 'ofehc': 53, 'vrwrf': 15}


def func2():
    return (2, 83, 80)


def func3():
    return [34, 37, 92]


def func4():
    return 12


def func5():
    return 96.53


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
