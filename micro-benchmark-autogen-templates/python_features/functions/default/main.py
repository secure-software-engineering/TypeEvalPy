# Defining a function with default values for its parameters.
def my_func(
    x=<value1>,
    y=<value1>
):
    return x + y


result1 = my_func(<value2>, <value2>)
result2 = my_func()
result3 = my_func(x=<value1>)
