# Defining a function with default values for its parameters.
def my_func(x=88, y=88):
    return x + y


result1 = my_func(96.81, 96.81)
result2 = my_func()
result3 = my_func(x=88)
