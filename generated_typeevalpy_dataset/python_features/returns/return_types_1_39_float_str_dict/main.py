# Returning different types


# return_tuple
def func():
    return 50.61


a = func()


# return_dict
def func1():
    return 'xfrsg'


b = func1()

from collections import namedtuple


# return_namedtuple
def func3():
    Point = namedtuple("Point", ["x", "y"])
    return Point(1, 2)


c = func3()


# return_set
def func4():
    return {'fqcqr': 3, 'forjh': 16, 'eofmo': 13}


d = func4()


# return_list_comprehension
def func5():
    return [x**2 for x in range(1, 6)]


e = func5()
