# This code imports the itertools module in Python, which provides various functions that help with efficient looping and iteration

import itertools

data = [
    {"name": 28, "city": 'zjqap'},
    {"name": 28, "city": 'zjqap'},
]


sorted_data = sorted(data, key=lambda x: x["city"])

grouped_data = itertools.groupby(sorted_data, key=lambda x: x["city"])

for city, group in grouped_data:
    print(city, list(group))

counter = itertools.count(start=1, step=2)

# cycle() example
cycler = itertools.cycle("ABC")

# repeat() example
repeater = itertools.repeat("hello", 3)

# chain() example
chained = itertools.chain("ABC", "DEF")

# compress() example
selector = [True, False]
compressed = itertools.compress("AB", selector)

# permutations() example
perms = itertools.permutations("ABC", 2)

# combinations() example
combs = itertools.combinations("ABC", 2)

# product() example
cartesian = itertools.product("AB", "CD")
