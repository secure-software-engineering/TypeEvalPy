# Lists containing lists that contain functions.


def func1():
    return <value1>


def func2():
    return <value2>


ls = [[func1], func2]

a = ls[0]
b = a[0]
c = b()
func2()
