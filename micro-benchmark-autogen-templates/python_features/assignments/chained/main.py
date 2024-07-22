# Two variables are assigned a function via chained assignment.


def func1():
    return <value1>


def func2():
    return <value2>


a = b = func1

c = b()

a = b = func2

d = a()
