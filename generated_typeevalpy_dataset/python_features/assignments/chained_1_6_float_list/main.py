# Two variables are assigned a function via chained assignment.


def func1():
    return 74.62


def func2():
    return [26, 34, 83]


a = b = func1

c = b()

a = b = func2

d = a()
