# A new list is created as a slice of another one containing functions.


def func1():
    return 21.45


def func2():
    return [93, 77, 25]


def func3():
    return (76, 88, 40)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
