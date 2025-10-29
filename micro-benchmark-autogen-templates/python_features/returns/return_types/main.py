# Returning different types


# return_tuple
def func():
    return <value1>


a = func()


# return_dict
def func1():
    return <value2>


b = func1()

from collections import namedtuple


# return_namedtuple
Point = namedtuple("Point", ["x", "y"])
def func3():
    return Point(1, 2)


c = func3()


# return_set
def func4():
    return <value3>


d = func4()


# return_list_comprehension
def func5():
    return [x**2 for x in range(1, 6)]


e = func5()
