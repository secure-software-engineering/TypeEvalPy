# Two variables are assigned a function via chained assignment.


def func1():
    return [92, 63, 20]


def func2():
    return 25


a = b = func1

c = b()

a = b = func2

d = a()
