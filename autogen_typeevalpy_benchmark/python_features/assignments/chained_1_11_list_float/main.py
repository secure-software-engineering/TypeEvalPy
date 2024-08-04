# Two variables are assigned a function via chained assignment.


def func1():
    return [38, 28, 8]


def func2():
    return 58.34


a = b = func1

c = b()

a = b = func2

d = a()
