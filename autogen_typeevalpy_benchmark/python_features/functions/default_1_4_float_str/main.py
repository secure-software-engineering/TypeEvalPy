# Defining a function with default values for its parameters.
def my_func(x=55.41, y=55.41):
    return x + y


result1 = my_func('bkulv', 'bkulv')
result2 = my_func()
result3 = my_func(x=55.41)
