# Two variables are assigned a function via chained assignment.


def func1():
    return 86.27


def func2():
    return [71, 13, 7]


a = b = func1

c = b()

a = b = func2

d = a()
