# A simple Python program that defines a function called 'arithmetic_op'.
# The function takes two integer parameters 'a' and 'b', adds them together and returns.
# The code is flow-sensitive because it changes its type of 'result' based on the flow of the program execution.

a = 2
b = 1
value = a + b
result = None
if value >= 5:
    result = value
else:
    result = "Less than or equal 5"

result = result

a = 3.0
b = 2.0
value = a + b
result = None
if value >= 5:
    result = value
else:
    result = "Less than or equal 5"

result = result
