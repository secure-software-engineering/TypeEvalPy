# Two variables are assigned a function via chained assignment.


def func1():
    return 94


def func2():
    return [44, 14, 32]


a = b = func1

c = b()

a = b = func2

d = a()
