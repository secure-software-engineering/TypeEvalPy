# Function which has a combined return type [int,str]
# The given code is context sensitive because it produces different results based on the context in which it is executed.


def my_function(my_bool):
    if my_bool:
        x = 5
    else:
        x = "Hello World!"
    return x


result1 = my_function(False)
result2 = my_function(0)

result3 = my_function(True)
result4 = my_function(1)
result5 = my_function("Y")
