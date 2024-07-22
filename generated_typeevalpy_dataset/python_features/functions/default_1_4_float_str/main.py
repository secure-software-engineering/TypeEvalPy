# Defining a function with default values for its parameters.
def my_func(x=94.58, y=94.58):
    return x + y


result1 = my_func('qsnsr', 'qsnsr')
result2 = my_func()
result3 = my_func(x=94.58)
