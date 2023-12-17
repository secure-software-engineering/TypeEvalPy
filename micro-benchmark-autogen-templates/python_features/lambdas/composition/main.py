# Chaining multiple function calls using lambda functions.


result = (lambda x: x + 1)((lambda x: x * 2)(5))
