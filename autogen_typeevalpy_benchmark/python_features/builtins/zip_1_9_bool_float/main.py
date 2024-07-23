# The zip function in Python takes two or more iterables and returns an iterator that aggregates elements from each of the iterables.
# In this example, two lists names and ages are passed to zip function to combine the corresponding elements of the two lists into tuples
names = [True, True]

ages = [51.78, 51.78]

combined = zip(names, ages)

result = list(combined)
