# A new list is created as a slice of another one containing functions.


def func1():
    return <value1>


def func2():
    return <value2>


def func3():
    return <value3>


ls = [func1, func2, func3]

ls2 = ls[1:3]

c = ls2[0]()
