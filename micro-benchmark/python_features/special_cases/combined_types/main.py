# Function which has a combined return type [int,str]
def my_function(my_bool):
    if my_bool:
        x = 5
    else:
        x = "Hello World!"
    return x


a = my_function(True)
b = my_function(False)
