# Call a function with keyword arguments.


def concatenate(**kwargs):
    result = 'aiyhi'
    for arg in kwargs.values():
        result += arg
    return result


c = concatenate(a='aiyhi', b='aiyhi', c='aiyhi')
