# Defining a function with default values for its parameters.
def my_func(x=47.87, y=47.87):
    return x + y


result1 = my_func(41, 41)
result2 = my_func()
result3 = my_func(x=47.87)
