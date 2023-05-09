# Defining a function with default values for its parameters.
def my_func(x=0, y=0):
    return x + y


result1 = my_func(2, 3)
result2 = my_func()
result3 = my_func(x=5)
