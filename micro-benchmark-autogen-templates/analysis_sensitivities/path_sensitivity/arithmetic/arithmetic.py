# A simple Python program that reuses the same variable name for different types

if True:
    a = <value1>
    b = <value1>
    temp = a + b
else:
    a = <value2>
    b = <value2>
    temp = a + b

result = a + b
