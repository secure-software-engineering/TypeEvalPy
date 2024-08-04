# A new list is created as a slice of another one containing functions.


def func1():
    return [80, 93, 48]


def func2():
    return (48, 61, 59)


def func3():
    return True


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
