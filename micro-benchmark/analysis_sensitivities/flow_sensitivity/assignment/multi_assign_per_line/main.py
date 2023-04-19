# Three variables are assigned a value via a recursive tuple assignment.


def func1():
    return 42


def func2():
    return "Hello from func2"


assign_1, assign_2 = func1, func2
a = assign_1()
b = assign_2() 

assign_1, assign_2 = func2, func1
c = assign_1()
d = assign_2()