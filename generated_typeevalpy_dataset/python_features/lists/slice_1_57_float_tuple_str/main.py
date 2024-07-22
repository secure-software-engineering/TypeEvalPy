# A new list is created as a slice of another one containing functions.


def func1():
    return 14.52


def func2():
    return (39, 89, 65)


def func3():
    return 'vlwpp'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
