# Call a function with keyword arguments.


def concatenate(**kwargs):
    result = 'dlfln'
    for arg in kwargs.values():
        result += arg
    return result


c = concatenate(a='dlfln', b='dlfln', c='dlfln')
