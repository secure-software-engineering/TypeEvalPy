# The zip function in Python takes two or more iterables and returns an iterator that aggregates elements from each of the iterables.
# In this example, two lists names and ages are passed to zip function to combine the corresponding elements of the two lists into tuples
names = [43, 43]

ages = ['iyrpm', 'iyrpm']

combined = zip(names, ages)

result = list(combined)
