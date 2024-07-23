# Two variables are assigned a function via chained assignment.


def func1():
    return 94.76


def func2():
    return [92, 86, 78]


a = b = func1

c = b()

a = b = func2

d = a()
