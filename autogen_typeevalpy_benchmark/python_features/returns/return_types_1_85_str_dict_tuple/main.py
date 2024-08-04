# Returning different types


# return_tuple
def func():
    return 'alvwc'


a = func()


# return_dict
def func1():
    return {'zigtv': 14, 'ecggx': 8, 'pmpdd': 92}


b = func1()

from collections import namedtuple


# return_namedtuple
def func3():
    Point = namedtuple("Point", ["x", "y"])
    return Point(1, 2)


c = func3()


# return_set
def func4():
    return (70, 6, 57)


d = func4()


# return_list_comprehension
def func5():
    return [x**2 for x in range(1, 6)]


e = func5()
