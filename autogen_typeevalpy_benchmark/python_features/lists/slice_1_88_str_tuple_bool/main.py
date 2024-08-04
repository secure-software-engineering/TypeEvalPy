# A new list is created as a slice of another one containing functions.


def func1():
    return 'stvdw'


def func2():
    return (9, 29, 7)


def func3():
    return True


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
