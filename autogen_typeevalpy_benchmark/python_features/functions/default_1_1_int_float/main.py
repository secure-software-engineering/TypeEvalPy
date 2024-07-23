# Defining a function with default values for its parameters.
def my_func(x=71, y=71):
    return x + y


result1 = my_func(33.49, 33.49)
result2 = my_func()
result3 = my_func(x=71)
