# Defining a function with default values for its parameters.
def my_func(x=32, y=32):
    return x + y


result1 = my_func(83.71, 83.71)
result2 = my_func()
result3 = my_func(x=32)
