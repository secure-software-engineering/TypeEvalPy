# A simple Python program that reuses the same variable name for different types

if True:
    a = 1
    b = 2
    temp = a + b
else:
    a = 1.0
    b = 2.0
    temp = a + b

result = a + b
