# A new list is created as a slice of another one containing functions.


def func1():
    return False


def func2():
    return 'shhsh'


def func3():
    return (8, 36, 65)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
