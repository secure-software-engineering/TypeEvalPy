# A Python program that defines a function called 'my_function' with combined return types.
# The given code is flow-sensitive because it produces different results based on the flow of the program execution.

my_bool = False
value = None
if my_bool:
    value = 5
else:
    value = "Hello world"

result = value

my_bool = True
value = None
if my_bool:
    value = 5
else:
    value = "Hello world"

result = value
