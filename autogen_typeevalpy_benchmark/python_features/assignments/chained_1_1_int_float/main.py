# Two variables are assigned a function via chained assignment.


def func1():
    return 46


def func2():
    return 42.93


a = b = func1

c = b()

a = b = func2

d = a()
