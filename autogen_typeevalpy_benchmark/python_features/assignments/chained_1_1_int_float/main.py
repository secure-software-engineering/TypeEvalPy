# Two variables are assigned a function via chained assignment.


def func1():
    return 67


def func2():
    return 94.04


a = b = func1

c = b()

a = b = func2

d = a()
