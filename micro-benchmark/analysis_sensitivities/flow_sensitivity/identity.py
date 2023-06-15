# A Python program that defines a function called 'identity' which will simply return the variable, but also performs type checking and casting.
# The given code is flow sensitive because it produces different results based on the flow of the program execution.

x = 5
value = None
if isinstance(x, str):
    value = str(x)
elif isinstance(x, int):
    value = int(x)
elif isinstance(x, float):
    value = float(x)
else:
    value = x

result = value

x = "Hello"
value = None
if isinstance(x, str):
    value = str(x)
elif isinstance(x, int):
    value = int(x)
elif isinstance(x, float):
    value = float(x)
else:
    value = x

result = value
