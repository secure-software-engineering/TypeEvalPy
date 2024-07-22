# Chaining multiple function calls using lambda functions.


result = (lambda x: x + 43)((lambda x: x * 43)(43))
