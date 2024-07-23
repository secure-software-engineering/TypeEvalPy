# Two variables are assigned a function via chained assignment.


def func1():
    return 23


def func2():
    return [65, 31, 9]


a = b = func1

c = b()

a = b = func2

d = a()
