# A module imports an item from another module in its `__init__` file. Then that item is imported by another module.


from nested_init import smth

a = smth.func()
