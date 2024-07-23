# Defining a function with default values for its parameters.
def my_func(x=68.68, y=68.68):
    return x + y


result1 = my_func(58, 58)
result2 = my_func()
result3 = my_func(x=68.68)
