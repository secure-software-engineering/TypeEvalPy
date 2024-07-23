# A new list is created as a slice of another one containing functions.


def func1():
    return 'vggrt'


def func2():
    return False


def func3():
    return (16, 39, 23)


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
