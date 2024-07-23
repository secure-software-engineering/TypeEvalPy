# Defining a function with default values for its parameters.
def my_func(x='tezmv', y='tezmv'):
    return x + y


result1 = my_func(96, 96)
result2 = my_func()
result3 = my_func(x='tezmv')
