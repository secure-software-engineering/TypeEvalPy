# Defining a function with default values for its parameters.
def my_func(x=52.7, y=52.7):
    return x + y


result1 = my_func(59, 59)
result2 = my_func()
result3 = my_func(x=52.7)
