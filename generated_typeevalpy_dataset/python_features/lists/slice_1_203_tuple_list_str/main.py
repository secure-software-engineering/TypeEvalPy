# A new list is created as a slice of another one containing functions.


def func1():
    return (93, 65, 87)


def func2():
    return [10, 37, 50]


def func3():
    return 'gjwzt'


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
