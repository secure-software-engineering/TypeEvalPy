# Returning different types


# return_tuple
def func():
    return [47, 36, 6]


a = func()


# return_dict
def func1():
    return (62, 13, 97)


b = func1()

from collections import namedtuple


# return_namedtuple
def func3():
    Point = namedtuple("Point", ["x", "y"])
    return Point(1, 2)


c = func3()


# return_set
def func4():
    return 91


d = func4()


# return_list_comprehension
def func5():
    return [x**2 for x in range(1, 6)]


e = func5()
