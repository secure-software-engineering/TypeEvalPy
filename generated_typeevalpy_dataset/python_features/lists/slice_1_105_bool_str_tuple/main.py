# A new list is created as a slice of another one containing functions.


def func1():
    return True


def func2():
    return 'izquj'


def func3():
    return (24, 46, 27)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
