# Chaining multiple function calls using lambda functions.


result = (lambda x: x + 6)((lambda x: x * 6)(6))
