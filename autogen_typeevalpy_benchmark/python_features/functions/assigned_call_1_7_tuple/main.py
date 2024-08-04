# A function is defined, assigned to a variable and called via that variable.


def func():
    return (39, 33, 59)


a = func
b = a()
