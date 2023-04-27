#

import itertools

data = [
    {"name": "Alice", "age": 30, "city": "New York"},
    {"name": "Bob", "age": 25, "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "city": "New York"},
    {"name": "David", "age": 40, "city": "San Francisco"},
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
selector = [True, False, True, False]
compressed = itertools.compress("ABCD", selector)

# permutations() example
perms = itertools.permutations("ABC", 2)

# combinations() example
combs = itertools.combinations("ABC", 2)

# product() example
cartesian = itertools.product("AB", "CD")
